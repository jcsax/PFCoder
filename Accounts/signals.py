from django.db.models.signals import post_save
from django.contrib.auth.models import User
from Accounts.models import Profile
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)