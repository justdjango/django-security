from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django_otp.admin import OTPAdminSite


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('djoser.urls')),
    path('secret-admin/', admin.site.urls),
    path('', include('accounts.urls', namespace='columns'))
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

if not settings.DEBUG:
    admin.site.__class__ = OTPAdminSite
admin.site.site_title = "Django Security Tutorial"
admin.site.site_header = "Django Security Tutorial"
