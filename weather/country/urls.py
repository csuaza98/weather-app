from django.urls import path
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Country
from .serializers import CountrySerializer

urlpatterns = [

    path('countries', ListCreateAPIView.as_view(queryset=Country.objects.all(), serializer_class=CountrySerializer),
         name='country-g'),
    path('countries/<int:pk>', RetrieveUpdateDestroyAPIView.as_view(queryset=Country.objects.all(), lookup_field='pk',
                                                                 serializer_class=CountrySerializer), name='country-gpd'),
    path('countries', CreateAPIView.as_view(serializer_class=CountrySerializer), name='country-p'),

]
