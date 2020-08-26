from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    AddPostView,
    AddCommentView
)
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('about/', views.about, name = 'blog-about'),
    path('articleSearch/', views.articleSearch, name='articleSearch'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name = 'add_comment'),
]
