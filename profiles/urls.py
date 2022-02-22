from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]