from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from .managers import UserManager


class User(AbstractUser):

    email = models.EmailField(unique=True, max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # option 1
    # e.g Staff, Client, Manager, etc.
    # user_type = models.CharField(max_length=100)

    # # option 2
    # is_client = models.BooleanField(default=True)
    # is_manager = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # fields, properties, user types
    user_type = models.CharField(max_length=100, choices=(
        ("Reader", "Reader"),
        ("Writer", "Writer"),
        ("Coordinator", "Coordinator"),
        ("Moderator", "Moderator")
    ), default='Reader')

    def __str__(self):
        return self.user.email


class Column(models.Model):
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
    writers = models.ManyToManyField(
        User, related_name='writers_columns')
    moderators = models.ManyToManyField(
        User, related_name='moderators_columns')

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    writer = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Subscription(models.Model):
    """This is the link between a user and a column that they're subscribed to"""
    reader = models.ForeignKey(
        User, related_name='user_subscriptions', on_delete=models.CASCADE)
    column = models.ForeignKey(
        Column, related_name='column_subscriptions', on_delete=models.CASCADE)

    def __str__(self):
        return self.reader.email


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_save_user_receiver, sender=User)
