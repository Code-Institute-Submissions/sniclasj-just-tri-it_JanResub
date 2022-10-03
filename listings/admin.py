from django.contrib import admin
from .models import Listing, Category, Condition


admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Condition)
