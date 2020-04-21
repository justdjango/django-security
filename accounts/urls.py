from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.ColumnListView.as_view(), name='column-list'),
    path('feed/', views.ColumnFeedView.as_view(), name='feed'),
    path('moderator/posts/', views.ModeratorPostListView.as_view(),
         name='moderator-post-list'),
    path('moderator/posts/<pk>/mark-as-public/',
         views.ModeratorMarkAsPublic.as_view(), name='mark-as-public'),
    path('posts/<pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('columns/<pk>/', views.ColumnDetailView.as_view(), name='column-detail'),
    path('create/column/', views.ColumnCreateView.as_view(), name='column-create'),
    path('create/post/', views.PostCreateView.as_view(), name='post-create'),
]
