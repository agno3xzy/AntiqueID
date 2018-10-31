from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'index'),
    path('test/', views.index, name = 'bootstrap_test'),
]
