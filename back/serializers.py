from rest_framework import serializers
from .models import BuildingType, Building


class BuildingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingType
        fields = ['id', 'name']


class BuildingSerializer(serializers.ModelSerializer):
    building_type = BuildingTypeSerializer()

    class Meta:
        model = Building
        fields = ['id', 'name', 'address', 'coordinates_latitude', 'coordinates_longitude', 'building_type']