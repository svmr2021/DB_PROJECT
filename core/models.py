from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Base(models.Model):
    """
    Base model to keep create, update times of every db object.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ElementBase(Base):
    """
    Base models for environment attributes (Air, Water, Animals..)
    """
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        abstract = True


class Client(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.company_name}'


class Employee(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identifier = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'{self.identifier}'


class Location(Base):
    country = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.country}-{self.region}'

    class Meta:
        ordering = ['-created_at',]


class Air(ElementBase):
    humidity = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    pressure = models.FloatField(default=0)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Air data'
        verbose_name_plural = 'Air info'


class Water(ElementBase):
    temperature = models.FloatField(default=0)
    radioactivity = models.FloatField(default=0)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Water data'
        verbose_name_plural = 'Water info'


class Soil(ElementBase):
    moisture = models.FloatField(default=0)
    salinity = models.FloatField(default=0)
    erosion = models.FloatField(default=0)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Soil data'
        verbose_name_plural = 'Soil info'


class Noise(ElementBase):
    level = models.FloatField(default=0)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Noise data'
        verbose_name_plural = 'Noise info'


class Plant(ElementBase):
    type = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Plant data'
        verbose_name_plural = 'Plant info'


class Animal(ElementBase):
    type = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Animal data'
        verbose_name_plural = 'Animal info'

