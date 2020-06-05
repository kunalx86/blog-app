from django.urls import path, re_path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, get_comments
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    re_path(r'^comments/$', get_comments, name='get_comments'),
    path('about/', views.about, name='blog-about')
]