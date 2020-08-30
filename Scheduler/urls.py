from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.options, name='options'),
    path('create', views.create, name = 'create'),
    path('read', views.read, name = 'read'),
    path('update', views.update, name = 'update'),
    path('delete', views.delete, name = 'delete'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout')
]
