# Generated by Django 4.1.3 on 2022-11-14 03:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_alter_classes_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2022, 11, 13, 22, 38, 30, 547344)),
        ),
    ]