from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django_otp.admin import OTPAdminSite
from accounts.views import home, session_requiring_view, LoginRequiredHomeView


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('secret-admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', LoginRequiredHomeView.as_view()),
    path('session/<payment_id>/', session_requiring_view, name='session-view'),
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

admin.site.__class__ = OTPAdminSite
admin.site.site_title = "Django Security Tutorial"
admin.site.site_header = "Django Security Tutorial"
