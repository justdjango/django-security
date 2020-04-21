from django.core.exceptions import PermissionDenied
from .models import Post


class ValidCoordinatorMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.userprofile.user_type != 'Coordinator':
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ValidWriterMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.userprofile.user_type != 'Writer':
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ValidModeratorMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.userprofile.user_type != 'Moderator':
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ModeratorHasAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['pk'])
        if request.user in post.column.moderators.all():
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied
