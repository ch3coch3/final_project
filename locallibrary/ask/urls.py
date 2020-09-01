from django.urls import path
from . import views
from .views import AskView,AskPostView,AskDetailView,AskCommentView


urlpatterns = [
    path('',AskView.as_view(),name='ask'),
    path('askpost/',AskPostView.as_view(),name='ask_post'),
    path('askpost/<int:pk>/', AskDetailView.as_view(), name = 'ask-detail'),
    path('ask/<int:pk>/comment', AskCommentView.as_view(), name = 'ask-comment'),
]