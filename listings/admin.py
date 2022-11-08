from django.contrib import admin
from .models import Listing, Category, Condition


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'lister', 'category', 'condition', 'price')


admin.site.register(Category)
admin.site.register(Condition)
