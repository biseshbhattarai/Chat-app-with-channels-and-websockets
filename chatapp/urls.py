from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',  auth_views.LoginView.as_view(), {'template_name': 'chatapp/login.html'}, name="login"),
    path('logout/',  auth_views.LogoutView.as_view(), {'template_name': 'chatapp/logout.html'}, name="logout"),
    path('register/', views.register, name="register"),
    path('chat/', views.index, name="index"),
    re_path(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room')
]
