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


class StaffTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffType
        fields = ['id', 'name']


class StaffSerializer(serializers.ModelSerializer):
    type = StaffTypeSerializer()

    class Meta:
        model = Staff
        fields = ['id', 'firstname', 'lastname', 'type', 'building', 'vehicle']


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
