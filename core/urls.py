from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from core.views import CountryListView, CountryDetailView, RegionDetailView, LocationDetailView, RegisterView

app_name = 'core'

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),
    path('countrylist/', CountryListView.as_view(), name='country_list'),
    path('country/detail/<int:pk>', CountryDetailView.as_view(), name='country_detail'),
    path('region/detail/<int:pk>', RegionDetailView.as_view(), name='region_detail'),
    path('location/detail/<int:pk>', LocationDetailView.as_view(), name='location_detail')
]