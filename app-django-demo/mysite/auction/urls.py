from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.auction, name='index'),
    path('auction_details/', views.auction_details, name='auction_details'),
    path('details/', views.details, name='details')
]
