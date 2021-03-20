from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    profile_pic = models.ImageField( upload_to='profilepics', default='profilepics/default.png')
    def __str__(self):
        return self.user.username

    
    