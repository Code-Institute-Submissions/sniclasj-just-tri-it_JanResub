from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Listing, Category, Condition
from .forms import ListingForm
from django.contrib import messages

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


def add_listing(request):
    """ Add a listing to the store """
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added listing!')
            return redirect(reverse('add_listing'))
        else:
            messages.error(
                request, 'Listing error. Please ensure the form is valid.')
    else:
        form = ListingForm()

    template = 'listings/add_listing.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
