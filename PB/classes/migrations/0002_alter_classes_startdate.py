# Generated by Django 4.1.3 on 2022-11-14 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2022, 11, 13, 19, 40, 10, 494526)),
        ),
    ]
