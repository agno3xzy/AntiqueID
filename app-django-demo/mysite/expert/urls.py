from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('detail/', views.detail, name = 'detail'),
    path('comment/', views.comment, name = 'comment'),
    path('comment_detail/', views.comment_detail, name = 'commnet_detail'),
]
