from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Profile
# from .forms import Form
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, athlete=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


def profile_admin(request):

    profiles = Profile.objects.all()

    context = {
        'profiles': profiles,
    }

    """A view to return the listings page"""
    return render(request, 'profiles/profile_admin.html', context)
