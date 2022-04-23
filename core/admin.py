from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Client)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name')


@admin.register(Employee)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'identifier')


@admin.register(Location)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('country', 'latitude', 'longitude', 'region')


@admin.register(Air)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('location', 'humidity', 'temperature', 'pressure')


@admin.register(Water)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('location', 'temperature', 'radioactivity')


@admin.register(Soil)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('location', 'moisture', 'salinity', 'erosion')


@admin.register(Noise)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('location', 'level')


@admin.register(Plant)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('location', 'type', 'amount')


@admin.register(Animal)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('location', 'type', 'amount')