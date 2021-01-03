from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Make, Car_Model, Model_Year, Engine, Fuel, Component, Part

# Create your views here.

class SearchResultsView(ListView):
    model = Part
    context_object_name = 'search_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        q1 = self.request.GET.get('a')
        q2 = self.request.GET.get('b')
        q3 = self.request.GET.get('c')
        q4 = self.request.GET.get('d')
        q5 = self.request.GET.get('e')
        search_list = Part.objects.filter(
            Q(make__name__iexact=q1),
            Q(car_model__name__iexact=q2),
            Q(model_year__prod_year__iexact=q3),
            Q(engine__name__iexact=q4),
            Q(fuel__name__iexact=q5)
        )
        return search_list

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