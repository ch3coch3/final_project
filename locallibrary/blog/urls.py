from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('register/', views.register, name = 'blog-register'),
    path('Login/', views.Login, name = 'blog-Login'),
    path('share/', views.share, name = 'blog-share'),
    path('forgetPass/', views.forgetPass, name = 'blog-forgetPass'),
    path('mainPage/', views.mainPage, name = 'blog-mainPage'),
]
