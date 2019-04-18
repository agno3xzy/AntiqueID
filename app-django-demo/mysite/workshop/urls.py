from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('allcomment/',views.allcomment, name = 'allcomment'),
    path('allexpert/',views.allexpert, name = 'allexpert'),
    path('apply/',views.apply, name = 'apply'),
]
