from django.test import Client, TestCase
from django.urls import reverse

from .models import Car, Component, Part

# Create your tests here.
class CarTests(TestCase):
    def setUp(self):
        self.car = Car.objects.create(
            name='BMW',
            model='1 series',
            year='2012',
            engine='1.6',
            fuel='petrol',
            slug='BMW',
        )

    def test_car_listing(self):
        self.assertEqual(f'{self.car.name}', 'BMW')
        self.assertEqual(f'{self.car.model}', '1 series')
        self.assertEqual(f'{self.car.year}', '2012')
        self.assertEqual(f'{self.car.engine}', '1.6')
        self.assertEqual(f'{self.car.fuel}', 'petrol')
        self.assertEqual(f'{self.car.slug}', 'bmw')

    def test_car_list_view(self):
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'BMW')
        self.assertTemplateUsed(response, 'inventory/car_list.html')

    def test_car_detail_view(self):
        response = self.client.get(self.car.get_absolute_url())
        no_response = self.client.get('/inventory/cars/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'BMW')
        self.assertTemplateUsed(response, 'inventory/car_detail.html')

'''
class ComponentTests(TestCase):

class PartTests(TestCase):
'''