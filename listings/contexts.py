from django.conf import settings
from django.shortcuts import get_object_or_404
from listings.models import Category
from listings.models import Condition


def category_list(request):
    return {
       'all_categories': Category.objects.all(),
    }


def condition_list(request):
    return {
       'all_conditions': Condition.objects.all(),
    }
