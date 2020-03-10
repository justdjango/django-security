from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from .managers import UserManager


class User(AbstractUser):

    username = None
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


# option 3
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # fields, properties, user types
    user_type = models.CharField(max_length=100, choices=(
        ('Staff', 'Staff'),
        ('Client', 'Client'),
        ('Manager', 'Manager')
    ), default='Client')


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_save_user_receiver, sender=User)
