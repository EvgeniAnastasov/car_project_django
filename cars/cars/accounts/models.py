from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from cars.accounts.managers import CarsUserManager


class CarsUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = CarsUserManager()


class Profile(models.Model):

    first_name = models.CharField(
        max_length=25,
        blank=True,
        validators=(
            MinLengthValidator(2),
        ),
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        validators=(
            MinLengthValidator(2),
        ),
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(0),
        ),
    )

    nationality = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(2),
        ),
    )

    total_cars = models.IntegerField(
        blank=True,
        default=0,
    )

    profile_image = CloudinaryField(
        "Image",
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:eco"},
        format="jpg",
    )

    user = models.OneToOneField(
        CarsUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name
