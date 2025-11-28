from django.urls import path
from blogs.apps import BloggingConfig
from blogs.views import *


app_name = BloggingConfig.name

urlpatterns = [
    path('posts/', PostsListView.as_view(), name='home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]