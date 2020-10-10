from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.options, name='options'),
    #Authentication
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    #Todo List
    path('create', views.create, name = 'create'),
    path('read', views.read, name = 'read'),
    path('deleteTodo/<int:deletion_id>/', views.delete, name='delete'),
    path('updateTodo/<int:updation_id>/', views.update, name='update'),
    path('accountDelete', views.AccDelete, name='AccountDelete'),
    #News
    path('news', views.news, name='news'),
    #API
    #USERS
    path('api/user-task-views', views.taskList),
    path('api/user-task-create', views.taskCreate),
    path('api/user-task-update/<str:pk>', views.taskUpdate),
    path('api/user-task-delete/<str:pk>', views.taskDelete),
    #ADMINS
    path('api/admin-users', views.UserList),
    path('api/admin-task-data', views.taskData),

    #Video Streaming
    path('vidstream', views.youtube, name='vidstream')
]