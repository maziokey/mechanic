from django.contrib import admin

from .models import Make, Car_Model, Model_Year, Engine, Fuel, Component, Part

# Register your models here.

class Car_ModelAdmin(admin.ModelAdmin):
    list_display = ("name", "make",)

class Model_YearAdmin(admin.ModelAdmin):
    list_display = ("prod_year", "make", "car_model",)

class EngineAdmin(admin.ModelAdmin):
    list_display = ("name", "make", "car_model", "model_year",)

class FuelAdmin(admin.ModelAdmin):
    list_display = ("name", "make", "car_model", "model_year", "engine",)

class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "make", "car_model", "model_year", "engine", "fuel",)

class PartAdmin(admin.ModelAdmin):
    list_display = ("name", "make", "car_model", "model_year", "engine", "fuel", "stock", "price",)

admin.site.register(Make)
admin.site.register(Car_Model, Car_ModelAdmin)
admin.site.register(Model_Year, Model_YearAdmin)
admin.site.register(Engine, EngineAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Part, PartAdmin)