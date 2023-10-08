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


class VehicleTypeList(generics.ListCreateAPIView):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class StaffTypeList(generics.ListCreateAPIView):
    queryset = StaffType.objects.all()
    serializer_class = StaffTypeSerializer


class StaffTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffType.objects.all()
    serializer_class = StaffTypeSerializer


class StaffList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class ScenarioTypeList(generics.ListCreateAPIView):
    queryset = ScenarioType.objects.all()
    serializer_class = ScenarioTypeSerializer


class ScenarioTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScenarioType.objects.all()
    serializer_class = ScenarioTypeSerializer


class ScenarioList(generics.ListCreateAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


class ScenarioDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


class CallList(generics.ListCreateAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer


class CallDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer