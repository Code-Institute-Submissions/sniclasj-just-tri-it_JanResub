from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('is_seller',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
