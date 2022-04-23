from django.db.models import Max, Min
from django.shortcuts import render

# Create your views here.
from django.views import generic
from core.models import *


class CountryListView(generic.ListView):
    model = Location
    template_name = 'index.html'
    context_object_name = 'countries'

    def get_queryset(self):
        queryset = Country.objects.filter(is_active=True)
        return queryset


class CountryDetailView(generic.DetailView):
    template_name = 'country_detail.html'
    context_object_name = 'country'

    def get_queryset(self):
        queryset = Country.objects.filter(is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        response = super().get_context_data()
        return response


class RegionDetailView(generic.DetailView):
    template_name = 'region_detail.html'
    context_object_name = 'region'

    def get_queryset(self):
        queryset = Region.objects.filter(is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        response = super().get_context_data()
        return response


class LocationDetailView(generic.DetailView):
    template_name = 'location_detail.html'
    context_object_name = 'location'

    def get_queryset(self):
        queryset = Location.objects.filter(is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        response = super().get_context_data()
        dates = dict()
        dates['air_date'] = self.object.air_set.aggregate(min_date=Min('date'), max_date=Max('date'))
        dates['water_date'] = self.object.water_set.aggregate(min_date=Min('date'), max_date=Max('date'))
        dates['soil_date'] = self.object.soil_set.aggregate(min_date=Min('date'), max_date=Max('date'))
        dates['noise_date'] = self.object.noise_set.aggregate(min_date=Min('date'), max_date=Max('date'))
        dates['plant_date'] = self.object.plant_set.aggregate(min_date=Min('date'), max_date=Max('date'))
        response['dates'] = dates
        return response
