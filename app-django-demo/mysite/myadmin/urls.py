from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('expertapply/', views.expertapply, name='expertapply'),
    path('mallmanagement/', views.mallmanagement, name='mallmanagement'),
    path('usermanagement/', views.usermanagement, name='usermanagement'),
    path('auctionmanagement/', views.auctionmanagement, name='auctionmanagement'),
    path('expert_detail/', views.expert_detail, name='expert_detail'),
    path('checkapply/', views.checkapply, name='checkapply'),
]
