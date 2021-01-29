from django.urls import path

from .views import calculate_distance_view

urlpatterns = [
    path('', calculate_distance_view, name="calculate_view"),
]
