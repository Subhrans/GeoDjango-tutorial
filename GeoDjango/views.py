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
    city,country,lat,long,internet_error=get_ip(my_ip)
    if internet_error==None:
        country=geolocator.geocode(country)
        print("country",country)
        print("city",city)
        print("lat",lat)
        print("long",long)
        location_lat_lon=(lat,long)

        # Initial Folium Map
        map = folium.Map(location=location_lat_lon, width=800, height=500)
        folium.CircleMarker(location=[lat,long],radius=50,tooltip=city['country_name'],fill=True,fill_color="#428bca").add_to(map)
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
            map = folium.Map(location=destination_lat_lon, width=800, height=500)
            folium.Marker(location=[lat,long],tooltip=destination_,icon=folium.Icon(color='red')).add_to(map)
            folium.Circle(location=[lat,long],radius=10,tooltip=destination_).add_to(map)
            # folium.FeatureGroup(destination_lat_lon)
            map.fit_bounds(destination_lat_lon,location_lat_lon)
            # map=folium.Map()

            print(destination)
            instance.location="Asansol"
            instance.distance=50.00
            # Folium Map modification
            # instance.save()
            print(instance.destination)

        map=map._repr_html_()
    else:
        internet_error="Please connect Your Internet"
    context = {'distance': obj,
               'form':mform,
               'map':map,
               'internet_error':internet_error,
               }
    return render(request, 'Measurements/measurements.html', context)
