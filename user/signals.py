from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def buildProfile(sender,instance,created,**kwargs):
    if created:
        userprofile = Profile.objects.create(user= instance)
        userprofile.save()
