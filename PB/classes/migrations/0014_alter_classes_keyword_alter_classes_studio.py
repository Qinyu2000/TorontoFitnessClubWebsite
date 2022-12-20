# Generated by Django 4.1.3 on 2022-11-16 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0011_remove_studio_location_studio_lat_studio_lon_and_more'),
        ('classes', '0013_alter_classes_studio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='keyword',
            field=models.ManyToManyField(blank=True, to='classes.keyword'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='studios.studio'),
        ),
    ]