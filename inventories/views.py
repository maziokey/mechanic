from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Make, Car_Model, Model_Year, Engine, Fuel, Component, Part

# Create your views here.
class MakeListView(ListView):
    model = Make
    context_object_name = 'make_list'
    template_name = 'inventory/make_list.html'

class ComponentListView(ListView):
    model = Component
    context_object_name = 'component_list'
    template_name = 'inventory/component_list.html'

class PartListView(ListView):
    model = Part
    context_object_name = 'part_list'
    template_name = 'inventory/part_list.html'

class MakeDetailView(DetailView):
    model = Make
    context_object_name = 'make'
    template_name = 'inventory/make_detail.html'

class ComponentDetailView(DetailView):
    model = Component
    context_object_name = 'component'
    template_name = 'inventory/component_detail.html'

class PartDetailView(DetailView):
    model = Part
    context_object_name = 'part'
    template_name = 'inventory/part_detail.html'