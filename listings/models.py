from django.db import models

# Create your models here.


class Category(model.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Listing(model.Model):
    category = models.ForeignKey(
        'Category', null=False, blank=False, on_delete=CASCADE)
    name = models.CharField(max_length=254)
    condition = models.ForeignKey(
        'Condition', null=False, blank=False, on_delete=CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Condition(model.Model):
    status = models.CharField(max_length=254)

    def __str__(self):
        return self.status
