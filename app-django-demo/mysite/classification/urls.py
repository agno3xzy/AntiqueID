from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('result/', views.result, name = 'result'),
    path('color_mind/', views.color_mind, name = 'color_mind'),
    path('logout/', views.logout, name = 'logout'),
    path('upload_file/', views.upload_file, name = 'upload_file'),
]
