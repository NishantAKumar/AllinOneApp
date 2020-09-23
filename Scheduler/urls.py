from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.options, name='options'),
    path('create', views.create, name = 'create'),
    path('read', views.read, name = 'read'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('deleteTodo/<int:deletion_id>/', views.delete, name='delete'),
    path('updateTodo/<int:updation_id>/', views.update, name='update'),
    path('accountDelete', views.AccDelete, name='AccountDelete'),
    #news
     path('news', views.news, name='news')
]
