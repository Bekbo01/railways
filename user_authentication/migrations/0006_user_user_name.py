# Generated by Django 3.2.11 on 2022-09-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0005_alter_user_user_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.TextField(null=True, verbose_name='Имя '),
        ),
    ]
