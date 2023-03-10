# Generated by Django 4.1.3 on 2022-11-14 00:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studios', '0010_alter_amenity_studio'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('coach', models.CharField(max_length=200)),
                ('capacity', models.PositiveIntegerField(default=0)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('startdate', models.DateField(default=datetime.datetime.now)),
                ('enddate', models.DateField()),
                ('studio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='studios.studio')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recurrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveIntegerField(default=0)),
                ('date', models.DateField()),
                ('targetclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targetclass', to='classes.classes')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollrecurrence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollrecurrence', to='classes.recurrence')),
                ('enrolluser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolluser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
