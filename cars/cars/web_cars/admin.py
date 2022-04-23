from django.contrib import admin

from cars.web_cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
