from django.contrib import admin
from django.urls import path
from . import  views
from .views import UserPostListView, PostDeleteView, PostListView, PostDetailView, PostCreateView, PostUpdateView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #<app>/<model>_<viewtype>.html
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),  # <app>/<model>_<viewtype>.html

    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

]