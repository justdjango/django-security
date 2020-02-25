from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
