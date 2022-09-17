from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
Choice = [
    ("ME", "Машинист"), 
    ("DD", "Дежурный ДЕПО"), 
]

class User(AbstractUser):
    user_img = models.ImageField(upload_to='USERIMG/',blank=True)
    user_position = models.TextField(
        max_length=2,
        choices=Choice,
        null=True, blank=True
    )

    def __str__(self): # __unicode__ on Python 2
        return self.username