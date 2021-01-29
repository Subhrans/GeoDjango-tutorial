from django.shortcuts import render, get_object_or_404

from .forms import MeasurementModelForm
from .models import Measurement


# Create your views here.
def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    mform = MeasurementModelForm(request.POST or None)
    if mform.is_valid():
        instance=mform.save(commit=False)
        instance.destination=mform.cleaned_data['destination']
        instance.location="Asansol"
        instance.distance=50.00
        instance.save()
        print(instance.destination)
    context = {'distance': obj,
               'form':mform,
               }
    return render(request, 'Measurements/measurements.html', context)
