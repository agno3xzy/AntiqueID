from django.conf.urls import url, include
from django.shortcuts import render, redirect
from . import views
from django.urls import path

urlpatterns = [
    path(r'signin/', views.signin, name = 'signin'),
    path(r'signup/', views.signup, name = 'signup'),
    path(r'massagepage/', views.massagepage, name = 'massagepage'),
    path(r'logout/', views.logout, name = 'logout'),
]