from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Profile
from .forms import ProfileForm
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

    """A view to return the profile_admin page"""
    return render(request, 'profiles/profile_admin.html', context)


@login_required
def edit_seller_status(request, profile_id):
    """ Edit a profile's seller status """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    profile = get_object_or_404(Profile, pk=profile_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Successfully updated profile seller status!')
            return redirect(reverse('profile_admin'))
        else:
            messages.error(
                request, 'Update error. Please ensure the form is valid.')
    else:
        form = ProfileForm(instance=profile)
        messages.info(request, f'You are editing {profile.athlete}')

    template = 'profiles/edit_seller_status.html'
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)
