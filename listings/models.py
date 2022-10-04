from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Listing(models.Model):
    category = models.ForeignKey(
        'Category', null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    lister = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    condition = models.ForeignKey(
        'Condition', null=False, blank=False, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Condition(models.Model):
    status = models.CharField(max_length=254)

    def __str__(self):
        return self.status
