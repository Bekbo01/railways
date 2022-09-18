from statistics import mode
from django.db import models
from tasks.models import Task
from treasuremap.fields import LatLongField
from user_authentication.models import User
# Create your models here.
class DepoCopy(models.Model):

    name = models.TextField('Пункт', null=True, blank=True)
    point = LatLongField(blank=True, null=True)
    member = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name


class Depo(models.Model):

    depochoice = models.ForeignKey(DepoCopy, on_delete=models.DO_NOTHING, null=True, blank=True)
    task = models.ForeignKey(Task, 
        verbose_name=('Link to task'), 
        on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField(null=True, blank=True)

    machine_eng_get = models.BooleanField("Приехал (machinist)" , default=False)
    machine_eng_pop = models.BooleanField("Выехал (machinist)", default=False)
    
    depo_eng_get = models.BooleanField("Приехал (depo)" , default=False)
    depo_eng_pop = models.BooleanField("Выехал (depo)", default=False)

