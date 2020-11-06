from django.urls import path

from .views import MakeListView, MakeDetailView, ComponentListView, ComponentDetailView, PartListView, PartDetailView

urlpatterns = [
    path('cars/', MakeListView.as_view(), name='make_list'),
    path('components/', ComponentListView.as_view(), name='component_list'),
    path('parts/', PartListView.as_view(), name='part_list'),

    path('cars/<str:slug>-<uuid:pk>', MakeDetailView.as_view(), name='make_detail'),
    path('components/<str:slug>-<uuid:pk>', ComponentDetailView.as_view(), name='component_detail'),
    path('parts/<str:slug>-<uuid:pk>', PartDetailView.as_view(), name='part_detail'),
]