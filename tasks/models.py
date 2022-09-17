from django.db import models
from user_authentication.models import User 


# Create your models here.
class Task(models.Model):
    work_at = models.DateTimeField("Явка на работу", null=True, blank=True)
    check_med = models.BooleanField("Прошел мед осмотр", null=True, blank=True)
    locomative_start = models.DateTimeField("Прием локоматива начало", null=True, blank=True)
    locomative_end = models.DateTimeField("Прием локоматива конец", null=True, blank=True)

    user_position = models.ForeignKey(User,
        max_length=20000,
        on_delete=models.DO_NOTHING
    )
    name = models.TextField("Название задания", null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    departer_time = models.DateTimeField("Время выезда ", null=True, blank=True)
    arriving_time = models.DateTimeField("", null=True, blank=True)
    locomative_pass = models.DateTimeField("Сдача локоматива", null=True, blank=True)
    complate_task = models.DateTimeField("Завершение работы", null=True, blank=True)

    def __str__(self):
        return self.name