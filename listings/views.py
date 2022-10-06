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
            listing = form.save()
            messages.success(request, 'Successfully added listing!')
            return redirect(reverse('listing_info', args=[listing.id]))
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


def edit_listing(request, listing_id):
    """ Edit a listing in the store """
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated listing!')
            return redirect(reverse('listing_info', args=[listing.id]))
        else:
            messages.error(
                request, 'Update error. Please ensure the form is valid.')
    else:
        form = ListingForm(instance=listing)
        messages.info(request, f'You are editing {listing.name}')

    template = 'listings/edit_listing.html'
    context = {
        'form': form,
        'listing': listing,
    }

    return render(request, template, context)


def delete_listing(request, listing_id):
    """ Delete a listing from the store """
    listing = get_object_or_404(Listing, pk=listing_id)
    listing.delete()
    messages.success(request, 'Listing deleted!')
    return redirect(reverse('listings'))
