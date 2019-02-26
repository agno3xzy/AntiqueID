from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.auction, name='index'),
    path('auction_details/', views.details, name='details'),
]
