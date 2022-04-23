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


class Employee(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identifier = models.PositiveIntegerField(unique=True)


class Location(Base):
    country = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    region = models.CharField(max_length=255)


class Air(ElementBase):
    humidity = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    pressure = models.FloatField(default=0)


class Water(ElementBase):
    temperature = models.FloatField(default=0)
    radioactivity = models.FloatField(default=0)


class Soil(ElementBase):
    moisture = models.FloatField(default=0)
    salinity = models.FloatField(default=0)
    erosion = models.FloatField(default=0)


class Noise(ElementBase):
    level = models.FloatField(default=0)


class Plant(ElementBase):
    type = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)


class Animal(ElementBase):
    type = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)

