from django.contrib import admin

from .models import Make, Car_Model, Model_Year, Engine, Fuel, Component, Part

# Register your models here.
admin.site.register(Make)
admin.site.register(Car_Model)
admin.site.register(Model_Year)
admin.site.register(Engine)
admin.site.register(Fuel)
admin.site.register(Component)
admin.site.register(Part)