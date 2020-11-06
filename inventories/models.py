import uuid
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Make(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    slug = models.SlugField(default='', editable=False, max_length=200, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('make_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Car_Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make = models.ForeignKey(Make, related_name='carmodels', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    slug = models.SlugField(default='', editable=False, max_length=200, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('car_model_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Model_Year(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car_model = models.ForeignKey(Car_Model, related_name='modelyears', on_delete=models.CASCADE)
    year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    slug = models.SlugField(default='', editable=False, max_length=200, null=False)

    def __str__(self):
        return self.year

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('model_year_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.year
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Engine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_year = models.ForeignKey(Model_Year, related_name='engines', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    slug = models.SlugField(default='', editable=False, max_length=200, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('engine_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Fuel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    engine = models.ForeignKey(Engine, related_name='fuels', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    slug = models.SlugField(default='', editable=False, max_length=200, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('fuel_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Component(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    slug = models.SlugField(default='', editable=False, max_length=200, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('component_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Part(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make = models.ForeignKey(Make, related_name='makeparts', on_delete=models.CASCADE)
    car_model = models.ForeignKey(Car_Model, related_name='carmodelparts', on_delete=models.CASCADE)
    model_year = models.ForeignKey(Model_Year, related_name='yearparts', on_delete=models.CASCADE)
    engine = models.ForeignKey(Engine, related_name='engineparts', on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, related_name='fuelparts', on_delete=models.CASCADE)
    component = models.ForeignKey(Component, related_name='componentparts', on_delete=models.CASCADE)
    name = models.CharField(max_length=40, db_index=True)
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='pics/', blank=True)
    slug = models.SlugField(default='', editable=False, max_length=200, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('part_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

'''
class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, db_index=True)
    model = models.CharField(max_length=30)
    year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    engine = models.CharField(max_length=20)
    fuel = models.CharField(max_length=20)
    slug = models.SlugField(default='', editable=False, max_length=200, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('car_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

'''