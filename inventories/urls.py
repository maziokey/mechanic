from django.urls import path

from .views import CarListView, CarDetailView, ComponentListView, ComponentDetailView, PartListView, PartDetailView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('components/', ComponentListView.as_view(), name='component_list'),
    path('parts/', PartListView.as_view(), name='part_list'),

    path('cars/<str:slug>-<uuid:pk>', CarDetailView.as_view(), name='car_detail'),
    path('components/<str:slug>-<uuid:pk>', ComponentDetailView.as_view(), name='component_detail'),
    path('parts/<str:slug>-<uuid:pk>', PartDetailView.as_view(), name='part_detail'),
]