from django.test import TestCase
from .models import Profile


class TestModels(TestCase):
    def test_is_seller_defaults_to_false(self):
        seller_status = Profile.is_seller.BooleanField(
            'Test Default Seller Status')
        self.assertFalse(seller_status.done)
