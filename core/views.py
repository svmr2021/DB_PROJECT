from django.contrib.auth import authenticate, login
from django.db.models import Max, Min
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from core.forms import RegistrationForm
from core.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class CountryListView(LoginRequiredMixin, generic.ListView):
    model = Location
    template_name = 'index.html'
    context_object_name = 'countries'

    def get_queryset(self):
        queryset = Country.objects.filter(is_active=True)
        return queryset


class CountryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'country_detail.html'
    context_object_name = 'country'

    def get_queryset(self):
        queryset = Country.objects.filter(is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        response = super().get_context_data()
        return response


class RegionDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'region_detail.html'
    context_object_name = 'region'

    def get_queryset(self):
        queryset = Region.objects.filter(is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        response = super().get_context_data()
        return response


class LocationDetailView(LoginRequiredMixin, generic.DetailView):
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


class RegisterView(generic.FormView):
    form_class = RegistrationForm
    template_name = 'sign_up.html'
    success_url = 'index.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            company_name = form.cleaned_data['company_name']
            user = authenticate(username=username, password=password)
            Client.objects.create(user=user, company_name=company_name)
            login(request, user)
            return redirect('core:country_list')
        return render(request, 'sign_up.html', {
            'form': form,
        })