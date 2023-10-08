from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(BuildingType)
admin.site.register(Building)

admin.site.register(VehicleType)
admin.site.register(Vehicle)

admin.site.register(StaffType)
admin.site.register(Staff)

admin.site.register(ScenarioType)
admin.site.register(Scenario)

admin.site.register(Call)
