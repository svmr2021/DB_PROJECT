from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Avg
from django.db.models.functions import Coalesce


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


class Country(Base):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Region(Base):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='regions')
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class Location(Base):
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='locations')
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.region.title} - {self.latitude} - {self.longitude}'

    class Meta:
        ordering = ['-created_at', ]
        # unique_together = (
        #     'region',
        #     'latitude',
        # )

    @property
    def avg(self):
        """
        Avg climate and biodiversity data of this location between dates
        :return:
        """

        result = dict()
        result['air_avg'] = self.air_set.aggregate(avg_humidity=Avg('humidity'), avg_temp=Avg('temperature'),
                                                   avg_pressure=Avg('pressure'))
        result['water_avg'] = self.water_set.aggregate(avg_temp=Avg('temperature'), avg_radio=Avg('radioactivity'))
        result['soil_avg'] = self.soil_set.aggregate(avg_moisture=Avg('moisture'), avg_salinity=Avg('salinity'),
                                                     avg_erosion=Avg('erosion'))
        result['noise_avg'] = self.noise_set.aggregate(avg_level=Avg('level'))
        result['plant_avg'] = self.plant_set.aggregate(avg_amount=Avg('amount'))
        result['animal_avg'] = self.animal_set.aggregate(avg_amount=Avg('amount'))
        return result


class Air(ElementBase):
    humidity = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    pressure = models.FloatField(default=0)

    class Meta:
        ordering = ['date', ]
        verbose_name = 'Air data'
        verbose_name_plural = 'Air info'


class Water(ElementBase):
    temperature = models.FloatField(default=0)
    radioactivity = models.FloatField(default=0)

    class Meta:
        ordering = ['date', ]
        verbose_name = 'Water data'
        verbose_name_plural = 'Water info'


class Soil(ElementBase):
    moisture = models.FloatField(default=0)
    salinity = models.FloatField(default=0)
    erosion = models.FloatField(default=0)

    class Meta:
        ordering = ['date', ]
        verbose_name = 'Soil data'
        verbose_name_plural = 'Soil info'


class Noise(ElementBase):
    level = models.FloatField(default=0)

    class Meta:
        ordering = ['date', ]
        verbose_name = 'Noise data'
        verbose_name_plural = 'Noise info'


class Plant(ElementBase):
    type = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)

    class Meta:
        ordering = ['date', ]
        verbose_name = 'Plant data'
        verbose_name_plural = 'Plant info'


class Animal(ElementBase):
    type = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)

    class Meta:
        ordering = ['date', ]
        verbose_name = 'Animal data'
        verbose_name_plural = 'Animal info'

