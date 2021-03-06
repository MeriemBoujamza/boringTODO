from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
 

class Task(models.Model):
    title = models.CharField(max_length = 200,default='')
    pub_date = models.DateTimeField(default= timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


