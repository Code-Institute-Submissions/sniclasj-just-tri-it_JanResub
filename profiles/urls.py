from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_profiles, name='profiles'),
    path('<int:profile_id>/', views.profile_info, name='profile_info'),
]
