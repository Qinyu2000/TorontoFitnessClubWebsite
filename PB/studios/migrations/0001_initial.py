# Generated by Django 4.1.3 on 2022-11-11 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('postal_code', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utils.location')),
            ],
        ),
        migrations.CreateModel(
            name='StudioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='PB/studios/images/')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='studios.studio')),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('quantity', models.PositiveIntegerField()),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='studios.studio')),
            ],
        ),
    ]
