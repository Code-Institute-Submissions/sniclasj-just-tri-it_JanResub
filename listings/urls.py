from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_listings, name='listings'),
    path('<int:listing_id>/', views.listing_info, name='listing_info'),
    path('add/', views.add_listing, name='add_listing'),
    path('edit/<int:listing_id>/', views.edit_listing, name='edit_listing'),
    path('delete/<int:listing_id>/', views.delete_listing, name='delete_listing'),  # noqa
    path('add_category/', views.add_category, name='add_category'),
    path('add_condition/', views.add_condition, name='add_condition'),
    path('categories_conditions/', views.category_condition_admin, name='categories_conditions'),
    path('edit_category/<int:category_id>', views.edit_category, name='edit_category'),
    path('edit_condition/<int:condition_id>', views.edit_condition, name='edit_condition'),
]
