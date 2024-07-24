from django.shortcuts import render
from .models import Car
from rest_framework import generics
from .serializer import carSerializer

# Create your views here.
class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = carSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = carSerializer

    

