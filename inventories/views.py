from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Car, Component, Part

# Create your views here.
class CarListView(ListView):
    model = Car
    context_object_name = 'car_list'
    template_name = 'inventory/car_list.html'

class ComponentListView(ListView):
    model = Component
    context_object_name = 'component_list'
    template_name = 'inventory/component_list.html'

class PartListView(ListView):
    model = Part
    context_object_name = 'part_list'
    template_name = 'inventory/part_list.html'

class CarDetailView(DetailView):
    model = Car
    context_object_name = 'car'
    template_name = 'inventory/car_detail.html'

class ComponentDetailView(DetailView):
    model = Component
    context_object_name = 'component'
    template_name = 'inventory/component_detail.html'

class PartDetailView(DetailView):
    model = Part
    context_object_name = 'part'
    template_name = 'inventory/part_detail.html'