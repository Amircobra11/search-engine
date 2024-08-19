from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/<int:pk>/edit/', views.article_update, name='article_update'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
]
