from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from accounts.views import home, session_requiring_view, LoginRequiredHomeView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', LoginRequiredHomeView.as_view()),
    path('session/<payment_id>/', session_requiring_view),
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
