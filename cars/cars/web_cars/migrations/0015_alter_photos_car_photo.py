# Generated by Django 4.0.3 on 2022-04-29 19:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_cars', '0014_alter_car_car_brand_alter_car_car_model_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='car_photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image'),
        ),
    ]
