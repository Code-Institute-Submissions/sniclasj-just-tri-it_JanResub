from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    athlete = models.OneToOneField(User, on_delete=models.CASCADE)
    is_seller = models.BooleanField(
        verbose_name='Is Seller?', null=False, default=False
    )

    def __str__(self):
        return self.athlete.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Profile.objects.create(athlete=instance)
    # Existing users: just save the profile
    instance.profile.save()
