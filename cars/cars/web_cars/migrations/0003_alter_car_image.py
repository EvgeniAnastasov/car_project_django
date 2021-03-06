# Generated by Django 4.0.3 on 2022-04-04 17:59

import cars.web_cars.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_cars', '0002_car_user_profile_alter_car_hp_alter_car_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mediafiles/', validators=[cars.web_cars.validators.MaxFileSizeInMbValidator(10)]),
        ),
    ]
