# Generated by Django 4.1.3 on 2022-11-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0005_alter_studioimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amenity',
            name='studio',
        ),
        migrations.AddField(
            model_name='amenity',
            name='studio',
            field=models.ManyToManyField(blank=True, null=True, related_name='amenities', to='studios.studio'),
        ),
    ]