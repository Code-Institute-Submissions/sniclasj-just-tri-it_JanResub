from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_listings, name='listings'),
    path('<int:listing_id>/', views.listing_info, name='listing_info'),
    path('add/', views.add_listing, name='add_listing'),
    path('edit/<int:listing_id>/', views.edit_listing, name='edit_listing'),
    path('delete/<int:listing_id>/', views.delete_listing, name='delete_listing'),
]
