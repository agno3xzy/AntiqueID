from django.conf.urls import url, include
from django.shortcuts import render, redirect
from . import views
from django.urls import path

urlpatterns = [
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    path('massagepage/', views.massagepage, name = 'massagepage'),
]