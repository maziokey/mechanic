from django.contrib import admin

from .models import Make, Car_Model, Model_Year, Engine, Fuel, Component, Part

# Register your models here.

class Car_ModelAdmin(admin.ModelAdmin):
    list_display = ("name", "make",)

class Model_YearAdmin(admin.ModelAdmin):
    list_display = ("prod_year", "car_model", "make",)

class EngineAdmin(admin.ModelAdmin):
    list_display = ("name", "model_year", "car_model", "make",)

class FuelAdmin(admin.ModelAdmin):
    list_display = ("name", "engine", "model_year", "car_model", "make",)

admin.site.register(Make)
admin.site.register(Car_Model, Car_ModelAdmin)
admin.site.register(Model_Year, Model_YearAdmin)
admin.site.register(Engine, EngineAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(Component)
admin.site.register(Part)