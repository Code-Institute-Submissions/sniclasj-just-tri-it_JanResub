from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('admin/', views.profile_admin, name='profile_admin'),
    path('admin/<int:profile_id>', views.edit_seller_status, name='edit_seller_status'),  # noqa
    path('order_history/<order_number>', views.order_history, name='order_history'),  # noqa
]
