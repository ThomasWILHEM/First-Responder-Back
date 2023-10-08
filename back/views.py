from .serializers import *
from rest_framework import generics

# Create your views here.


class BuildingTypeList(generics.ListCreateAPIView):
    queryset = BuildingType.objects.all()
    serializer_class = BuildingTypeSerializer


class BuildingTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildingType.objects.all()
    serializer_class = BuildingTypeSerializer


class BuildingList(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer