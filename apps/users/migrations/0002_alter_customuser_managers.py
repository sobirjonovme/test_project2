# Generated by Django 4.2 on 2023-05-06 09:13

import apps.users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', apps.users.models.CustomUserManager()),
            ],
        ),
    ]
