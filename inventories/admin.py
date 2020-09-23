from django.contrib import admin
from .models import Car, Component, Part

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "year",)



admin.site.register(Car, CarAdmin)
admin.site.register(Component)
admin.site.register(Part)