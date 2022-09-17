from django.db import models
from tasks.models import Task
# Create your models here.
class DepoCopy(models.Model):

    name = models.TextField('Пункт', null=True, blank=True)

    def __str__(self):
        return self.name


class Depo(models.Model):

    depochoice = models.ForeignKey(DepoCopy, on_delete=models.DO_NOTHING, null=True, blank=True)
    task = models.ForeignKey(Task, 
    verbose_name=('Link to task'), 
    on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField(null=True, blank=True)
    