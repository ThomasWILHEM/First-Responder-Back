from rest_framework import serializers
from .models import *


class BuildingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingType
        fields = ['id', 'name']


class BuildingSerializer(serializers.ModelSerializer):
    type = BuildingTypeSerializer()

    class Meta:
        model = Building
        fields = ['id', 'name', 'address', 'coordinates_latitude', 'coordinates_longitude', 'type']


class BuildingCreateSerializer(serializers.ModelSerializer):
    type_id = serializers.PrimaryKeyRelatedField(queryset=BuildingType.objects.all(), source='type', write_only=True)

    class Meta:
        model = Building
        fields = ('id', 'name', 'address', 'coordinates_latitude', 'coordinates_longitude', 'type_id')


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ['id', 'name']


class VehicleSerializer(serializers.ModelSerializer):
    type = VehicleTypeSerializer()

    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'coordinates_latitude', 'coordinates_longitude', 'type', 'building']


class VehicleCreateSerializer(serializers.ModelSerializer):
    type_id = serializers.PrimaryKeyRelatedField(queryset=VehicleType.objects.all(), source='type', write_only=True)
    building_id = serializers.PrimaryKeyRelatedField(queryset=Building.objects.all(), source='building', write_only=True)
    call_id = serializers.PrimaryKeyRelatedField(queryset=Call.objects.all(), source='call', write_only=True, allow_null=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'coordinates_latitude', 'coordinates_longitude', 'type_id', 'building_id', 'call_id']


class StaffTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffType
        fields = ['id', 'name']


class StaffSerializer(serializers.ModelSerializer):
    type = StaffTypeSerializer()

    class Meta:
        model = Staff
        fields = ['id', 'firstname', 'lastname', 'type', 'building', 'vehicle']


class StaffCreateSerializer(serializers.ModelSerializer):
    type_id = serializers.PrimaryKeyRelatedField(queryset=StaffType.objects.all(), source='type', write_only=True)
    building_id = serializers.PrimaryKeyRelatedField(queryset=Building.objects.all(), source='building', write_only=True)
    vehicle_id = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), source='vehicle', write_only=True, allow_null=True)

    class Meta:
        model = Staff
        fields = ['id', 'firstname', 'lastname', 'building_id', 'vehicle_id', 'type_id']


class ScenarioTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioType
        fields = ['id', 'name']


class ScenarioSerializer(serializers.ModelSerializer):
    type = ScenarioTypeSerializer()

    class Meta:
        model = Scenario
        fields = ['id', 'name', 'description', 'type']


class CallSerializer(serializers.ModelSerializer):
    scenario = ScenarioSerializer()

    class Meta:
        model = Call
        fields = ['id', 'coordinates_latitude', 'coordinates_longitude', 'datetime', 'completion_datetime',
                  'mission_status', 'scenario']


class CallWithRessourcesSerializer(serializers.ModelSerializer):
    scenario = ScenarioSerializer()
    vehicles_on_scene = VehicleSerializer(many=True)
    vehicles_available = serializers.SerializerMethodField()

    class Meta:
        model = Call
        fields = ['id', 'coordinates_latitude', 'coordinates_longitude', 'datetime', 'completion_datetime',
                  'mission_status', 'scenario', 'vehicles_on_scene', 'vehicles_available']

    def get_vehicles_available(self, obj):
        all_vehicles = Vehicle.objects.all()
        vehicles_on_scene = obj.vehicles_on_scene.all()
        vehicles_available = all_vehicles.exclude(id__in=[vehicle.id for vehicle in vehicles_on_scene])
        serializer = VehicleSerializer(vehicles_available, many=True)

        return serializer.data