from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    AddPostView,
    AddCommentView,
    AreaView,
    AreaCategoryView,
    
)
from ask.views import AskView,AskPostView,AskDetailView,AskCommentView
from newsboard import news_views
from newsboard.news_views import Newshome, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, AddArticleView
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
    path('area/<str:areas>/', AreaView, name = 'area'),
    path('area/<str:areas>/<str:cats>/', AreaCategoryView, name = 'area_category'),
    path('ask/',AskView.as_view(),name='ask'),
    path('askpost/',AskPostView.as_view(),name='ask_post'),
    path('askpost/<int:pk>/', AskDetailView.as_view(), name = 'ask-detail'),
    path('ask/<int:pk>/comment', AskCommentView.as_view(), name = 'ask-comment'),
    path('news/', Newshome.as_view(), name = 'newshome'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('add_article/', AddArticleView.as_view(), name = 'add_article'),
    path('article_search/', news_views.article_search, name='article_search'),
]
