from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('chat/', views.index, name="index"),
    re_path(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room')
]
