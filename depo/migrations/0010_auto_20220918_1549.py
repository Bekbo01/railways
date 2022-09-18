# Generated by Django 3.2.11 on 2022-09-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depo', '0009_auto_20220918_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depo',
            name='depo_eng_get',
            field=models.BooleanField(default=False, verbose_name='Приехал (depo)'),
        ),
        migrations.AlterField(
            model_name='depo',
            name='depo_eng_pop',
            field=models.BooleanField(default=False, verbose_name='Выехал (depo)'),
        ),
        migrations.AlterField(
            model_name='depo',
            name='machine_eng_get',
            field=models.BooleanField(default=False, verbose_name='Приехал (machinist)'),
        ),
        migrations.AlterField(
            model_name='depo',
            name='machine_eng_pop',
            field=models.BooleanField(default=False, verbose_name='Выехал (machinist)'),
        ),
    ]
