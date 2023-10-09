from rest_framework.response import Response

from .serializers import *
from rest_framework import generics, status


# Create your views here.


class BuildingTypeList(generics.ListCreateAPIView):
    queryset = BuildingType.objects.all()
    serializer_class = BuildingTypeSerializer


class BuildingTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildingType.objects.all()
    serializer_class = BuildingTypeSerializer


class BuildingList(generics.ListCreateAPIView):
    queryset = Building.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BuildingCreateSerializer
        return BuildingSerializer


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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return VehicleCreateSerializer
        return VehicleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        vehicle_obj = serializer.instance
        vehicle_with_type_serializer = VehicleSerializer(vehicle_obj)

        return Response(vehicle_with_type_serializer.data, status=status.HTTP_201_CREATED)


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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StaffCreateSerializer
        return StaffSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        staff_obj = serializer.instance
        staff_with_type_serializer = StaffSerializer(staff_obj)

        return Response(staff_with_type_serializer.data, status=status.HTTP_201_CREATED)


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


class CallDetailsWithRessources(generics.RetrieveUpdateDestroyAPIView):
    queryset = Call.objects.all()
    serializer_class = CallWithRessourcesSerializer


class VehiclesFromBuildingList(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        building_id = self.kwargs['building_id']
        queryset = Vehicle.objects.filter(building_id=building_id)
        return queryset


class StaffsFromBuildingList(generics.ListCreateAPIView):
    serializer_class = StaffSerializer

    def get_queryset(self):
        building_id = self.kwargs['building_id']
        queryset = Staff.objects.filter(building_id=building_id)
        return queryset


class SendVehiclesToCall(generics.UpdateAPIView):
    serializer_class = MultipleVehicles

    def update(self, request, *args, **kwargs):
        call_id = kwargs['pk']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicle_ids = serializer.validated_data['vehicles']

        try:
            call = Call.objects.get(pk=call_id)
        except Call.DoesNotExist:
            return Response({'error': 'Call with the given ID does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        vehicles_to_add = Vehicle.objects.filter(pk__in=vehicle_ids)

        # Associez les véhicules à l'appel
        call.vehicles_on_scene.add(*vehicles_to_add)

        return Response({'message': 'Vehicles added to call successfully.'}, status=status.HTTP_200_OK)



class VehicleQuitCall(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        vehicle_id = kwargs['pk']

        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            return Response({'error': 'Vehicle with the given ID does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        vehicle.call = None
        vehicle.save()

        return Response({'message': 'Vehicle association updated successfully.'}, status=status.HTTP_200_OK)
