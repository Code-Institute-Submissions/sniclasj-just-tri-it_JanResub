from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('admin/', views.profile_admin, name='profile_admin')
]
