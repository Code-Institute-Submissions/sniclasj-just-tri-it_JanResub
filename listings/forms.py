from django import forms
from .models import Listing, Category, Condition


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        condition = Condition.objects.all()
