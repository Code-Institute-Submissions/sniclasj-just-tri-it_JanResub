from django.shortcuts import render
from .models import Listing

# Create your views here.


def all_listings(request):

    listings = Listing.objects.all

    context = {
        'listings': listings,
    }

    """A view to return the index page"""
    return render(request, 'listings/listings.html', context)
