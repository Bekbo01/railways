from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser
#from depo.models import DepoCopy

# Create your models here.
Choice = [
    ("Машинист", "Машинист"), 
    ("Дежурный ДЕПО", "Дежурный ДЕПО"), 
]

class User(AbstractUser):
    user_name = models.TextField("Имя ", null=True)
    user_img = models.ImageField(upload_to='USERIMG/',blank=True)
    user_position = models.TextField(
        max_length=30,
        choices=Choice,
        null=True, blank=True
    )
    # user_depo = models.ForeignKey(DepoCopy, on_delete=models.DO_NOTHING, null=True)
    
