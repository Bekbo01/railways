from atexit import register
from django.contrib import admin
from .models import Task
from django.contrib.admin.options import TabularInline
from depo.models import Depo, DepoCopy

class DepoAdminInline(TabularInline):
    extra = 1
    model = Depo

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):

    inlines = (DepoAdminInline, )

admin.site.register(DepoCopy)
admin.site.register(Depo)
