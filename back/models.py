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

    type = models.ForeignKey(BuildingType, on_delete=models.CASCADE, related_name="buildings")

    def __str__(self):
        return f"{self.name} - {self.type.name}"


class VehicleType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    coordinates_latitude = models.FloatField()
    coordinates_longitude = models.FloatField()

    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, related_name="vehicles")
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, related_name="vehicles", null=True)

    def __str__(self):
        return f"{self.name} - {self.type.name}"


class StaffType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Staff(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    type = models.ForeignKey(StaffType, on_delete=models.CASCADE, related_name="vehicles")
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, related_name="staffs", null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, related_name="occupants", null=True)

    def __str__(self):
        return f"{self.name} - {self.type.name}"


class ScenarioType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    type = models.ForeignKey(ScenarioType, on_delete=models.CASCADE, related_name="scenarios")

    def __str__(self):
        return f"{self.name} - {self.type.name}"


class Call(models.Model):
    CALL_STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    coordinates_latitude = models.FloatField()
    coordinates_longitude = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True)
    completion_datetime = models.DateTimeField(null=True)
    mission_status = models.CharField(
        max_length=20,
        choices=CALL_STATUS_CHOICES,
        auto_created='not_started'
    )

    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name="calls")

    def __str__(self):
        return f"{self.scenario.name} - {self.mission_status}"
