# Generated by Django 3.2.15 on 2022-09-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depo', '0003_auto_20220917_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='depo',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]