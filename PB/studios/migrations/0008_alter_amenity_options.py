# Generated by Django 4.1.3 on 2022-11-11 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0007_alter_amenity_options_alter_amenity_studio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'amenities'},
        ),
    ]
