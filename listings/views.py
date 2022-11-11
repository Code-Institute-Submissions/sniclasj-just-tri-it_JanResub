from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Listing, Category, Condition
from .forms import ListingForm, CategoryForm, ConditionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_listings(request):

    listings = Listing.objects.all()
    categories = None
    conditions = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            listings = listings.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'condition' in request.GET:
            conditions = request.GET['condition'].split(',')
            listings = listings.filter(condition__status__in=conditions)
            conditions = Condition.objects.filter(status__in=conditions)

    context = {
        'listings': listings,
        'current_categories': categories,
        'current_conditions': conditions,
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


@login_required
def add_listing(request):
    """ Add a listing to the store """
    if not request.user.profile.is_seller:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.lister = request.user
            form.save()
            messages.success(request, 'Successfully added listing!')
            return redirect(reverse('listings'))
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


@login_required
def edit_listing(request, listing_id):
    """ Edit a listing in the store """
    if not request.user.profile.is_seller:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def delete_listing(request, listing_id):
    """ Delete a listing from the store """
    if not request.user.profile.is_seller:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    listing = get_object_or_404(Listing, pk=listing_id)
    listing.delete()
    messages.success(request, 'Listing deleted!')
    return redirect(reverse('listings'))


@login_required
def add_category(request):
    """ Add a category to the store """
    if not request.user.profile.is_seller:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cateogory = form.save()
            messages.success(request, 'Successfully added category!')
            return redirect(reverse('listings'))
        else:
            messages.error(
                request, 'Category error. Please ensure the form is valid.')
    else:
        form = CategoryForm()

    template = 'listings/add_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_category(request, category_id):
    """ Edit a category in the store """
    if not request.user.profile.is_seller:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated category!')
            return redirect(reverse('listings'))
        else:
            messages.error(
                request, 'Update error. Please ensure the form is valid.')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.name}')

    template = 'listings/edit_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@login_required
def add_condition(request):
    """ Add a condition to the store """
    if not request.user.profile.is_seller:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ConditionForm(request.POST)
        if form.is_valid():
            condition = form.save()
            messages.success(request, 'Successfully added condition!')
            return redirect(reverse('listings'))
        else:
            messages.error(
                request, 'Condition error. Please ensure the form is valid.')
    else:
        form = ConditionForm()

    template = 'listings/add_condition.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def category_condition_admin(request):

    categories = Category.objects.all()
    conditions = Condition.objects.all()

    template = 'listings/categories_conditions.html'
    context = {
        'categories': categories,
        'conditions': conditions,
    }

    """A view to return the category and condition admin page"""
    return render(request, template, context)
