from django import forms
from django.contrib.auth import get_user_model
from .models import Column, Post

User = get_user_model()


class PostForm(forms.ModelForm):
    column = forms.ModelChoiceField(queryset=Column.objects.none())

    class Meta:
        model = Post
        fields = ['title', 'column']

    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        user = User.objects.get(id=self.user_id)
        self.fields['column'].queryset = user.writers_columns.all()

    def clean(self):
        user = User.objects.get(id=self.user_id)
        data = self.cleaned_data
        column = data.get('column', None)
        if not column:
            raise forms.ValidationError("Please select a column")

        if column not in user.writers_columns.all():
            raise forms.ValidationError(
                "Please select a column you can write for")


class ColumnForm(forms.ModelForm):
    writers = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(userprofile__user_type='Writer'))
    moderators = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(userprofile__user_type='Moderator'))

    class Meta:
        model = Column
        fields = [
            'writers',
            'moderators',
            'name',
        ]

    def clean(self):
        data = self.cleaned_data

        writers = data.get('writers', None)
        moderators = data.get('moderators', None)

        if writers is None:
            raise forms.ValidationError("Please select a writer")

        if moderators is None:
            raise forms.ValidationError("Please select a moderator")

        writers_check = writers.filter(userprofile__user_type='Writer')
        if writers_check.count() != writers.count():
            raise forms.ValidationError(
                "Please ensure all the users are valid writers")

        moderators_check = moderators.filter(
            userprofile__user_type='Moderator')
        if moderators_check.count() != moderators.count():
            raise forms.ValidationError(
                "Please ensure all the users are valid writers")


class SubscribeForm(forms.Form):
    hidden = forms.HiddenInput()
