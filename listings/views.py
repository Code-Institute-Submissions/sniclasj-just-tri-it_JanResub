from django.shortcuts import render, get_object_or_404
from .models import Listing, Category

# Create your views here.


def all_listings(request):

    listings = Listing.objects.all()

    context = {
        'listings': listings,
    }

    """A view to return the listings page"""
    return render(request, 'listings/listings.html', context)


def listing_info(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }

    """A view to return the listing_info page"""
    return render(request, 'listings/listing_info.html', context)
