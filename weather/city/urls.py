from django.urls import path
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import City
from .serializers import CitySerializer

urlpatterns = [

    path('cities', ListCreateAPIView.as_view(queryset=City.objects.all(), serializer_class=CitySerializer),
         name='city-g'),
    path('cities/<int:pk>', RetrieveUpdateDestroyAPIView.as_view(queryset=City.objects.all(), lookup_field='pk',
                                                                 serializer_class=CitySerializer), name='city-gpd'),
    path('cities', CreateAPIView.as_view(serializer_class=CitySerializer), name='city-p'),

]
