from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Profile
# from .forms import Form
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_profiles(request):

    profiles = Profile.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'profiles/profiles.html', context)


def profile_info(request, profile_id):

    profile = get_object_or_404(Profile, pk=profile_id)

    context = {
        'profile': profile,
    }

    """A view to return the profile_info page"""
    return render(request, 'profiles/profile_info.html', context)
