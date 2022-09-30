from django.db import models


class Profile(models.Model):
    athlete = models.CharField(max_length=254)

    def __str__(self):
        return self.athlete
