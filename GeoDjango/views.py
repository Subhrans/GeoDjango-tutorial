from django.shortcuts import render, get_object_or_404
from geopy.geocoders import Nominatim
from .forms import MeasurementModelForm
from .models import Measurement
from .utils import get_ip
import folium
# Create your views here.


def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    mform = MeasurementModelForm(request.POST or None)
    geolocator=Nominatim(user_agent='GeoDjango')        # initialize app folder with nominatim

    my_ip='72.14.207.99'
    city,country,lat,long=get_ip(my_ip)
    country=geolocator.geocode(country)
    print("country",country)
    print("city",city)
    print("lat",lat)
    print("long",long)
    location_lat_lon=(lat,long)

    # Initial Folium Map
    map=folium.Map(location=location_lat_lon,width=800,height=500)
    if mform.is_valid():
        instance=mform.save(commit=False)
        # instance.destination=mform.cleaned_data['destination']
        destination_=mform.cleaned_data['destination']
        destination=geolocator.geocode(destination_)        # geocode function takes one or more location name and return all information about the location
        lat=destination.latitude
        long=destination.longitude
        print("lat: ",lat)
        print("long: ",long)
        destination_lat_lon=(lat,long)

        print(destination)
        instance.location="Asansol"
        instance.distance=50.00
        # Folium Map modification
        # instance.save()
        print(instance.destination)

    map=map._repr_html_()
    context = {'distance': obj,
               'form':mform,
               'map':map,
               }
    return render(request, 'Measurements/measurements.html', context)
