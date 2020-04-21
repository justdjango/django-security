from django.contrib import admin

from .models import User, UserProfile, Column, Subscription, Post

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Column)
admin.site.register(Subscription)
admin.site.register(Post)
