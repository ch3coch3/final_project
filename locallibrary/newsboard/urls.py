from django.urls import path
from newsboard import news_views
from newsboard import news_views
from newsboard.news_views import (
    Newshome, 
    ArticleDetailView, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDeleteView, 
    AddArticleView
)

urlpatterns = [
    path('', Newshome.as_view(), name = 'newshome'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('add_article/', AddArticleView.as_view(), name = 'add_article'),
    path('article_search/', news_views.article_search, name='article_search'),
]
