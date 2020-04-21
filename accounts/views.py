from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse, redirect, get_object_or_404
from .models import Column, Post, Subscription
from .forms import ColumnForm, PostForm, SubscribeForm
from .mixins import (
    ValidCoordinatorMixin, ValidWriterMixin, ValidModeratorMixin,
    ModeratorHasAccessMixin
)


class ColumnListView(generic.ListView):
    model = Column
    template_name = 'accounts/column_list.html'


class ColumnDetailView(generic.FormView):
    form_class = SubscribeForm
    template_name = 'accounts/column_detail.html'

    def get_success_url(self):
        return reverse("accounts:column-detail", kwargs={
            'pk': self.kwargs['pk']
        })

    def form_valid(self, form):
        if not self.request.user.userprofile.user_type == 'Reader':
            # message notification saying they cant subscribe
            return redirect(reverse("accounts:column-detail", kwargs={
                'pk': self.kwargs['pk']
            }))
        column = get_object_or_404(Column, id=self.kwargs['pk'])
        Subscription.objects.get_or_create(
            reader=self.request.user,
            column=column
        )
        return super(ColumnDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ColumnDetailView, self).get_context_data(**kwargs)
        column = Column.objects.get(id=self.kwargs['pk'])
        context['subscribed'] = False
        try:
            Subscription.objects.get(
                reader=self.request.user,
                column=column
            )
            context['subscribed'] = True
        except Subscription.DoesNotExist:
            pass
        context.update({
            "object": column
        })
        return context


class ColumnCreateView(LoginRequiredMixin, ValidCoordinatorMixin, generic.CreateView):
    model = Column
    form_class = ColumnForm
    template_name = 'accounts/column_create.html'

    def get_success_url(self):
        return reverse("columns:column-list")

    def form_valid(self, form):
        column = form.save(commit=False)
        column.coordinator = self.request.user
        column.save()
        return super(ColumnCreateView, self).form_valid(form)


class PostCreateView(LoginRequiredMixin, ValidWriterMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'accounts/post_create.html'

    def get_success_url(self):
        return reverse("columns:column-list")

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs.update({
            "user_id": self.request.user.id
        })
        return kwargs

    def form_valid(self, form):
        post = form.save(commit=False)
        post.writer = self.request.user
        post.save()
        return super(PostCreateView, self).form_valid(form)


class ModeratorPostListView(LoginRequiredMixin, ValidModeratorMixin, generic.ListView):
    template_name = 'accounts/moderator_post_list.html'

    def get_queryset(self):
        columns = list(
            self.request.user.moderators_columns.values_list('id', flat=True))
        qs = Post.objects.filter(column__id__in=columns)
        return qs


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'accounts/post_detail.html'


class ModeratorMarkAsPublic(LoginRequiredMixin, ValidModeratorMixin, ModeratorHasAccessMixin, generic.View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['pk'])
        post.public = True
        post.save()
        return redirect(reverse("accounts:post-detail", kwargs={'pk': kwargs['pk']}))


class ColumnFeedView(LoginRequiredMixin, generic.ListView):
    template_name = 'accounts/feed.html'

    def get_queryset(self):
        # return Subscription.objects.filter(reader=self.request.user)
        return self.request.user.user_subscriptions.all()
