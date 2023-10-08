from django.db import models

# Create your models here.


class BuildingType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    coordinates_latitude = models.FloatField()
    coordinates_longitude = models.FloatField()

    building_type = models.ForeignKey(BuildingType, on_delete=models.CASCADE, related_name="buildings")

    def __str__(self):
        return self.name
