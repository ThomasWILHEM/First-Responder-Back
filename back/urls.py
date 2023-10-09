from django.urls import path
from . import views

urlpatterns = [

    path('building-types', views.BuildingTypeList.as_view()),
    path('building-types/<int:pk>', views.BuildingTypeDetails.as_view()),
    path('buildings', views.BuildingList.as_view()),
    path('buildings/<int:pk>', views.BuildingDetails.as_view()),
    path('buildings/<int:building_id>/vehicles', views.VehiclesFromBuildingList.as_view()),
    path('buildings/<int:building_id>/staffs', views.StaffsFromBuildingList.as_view()),

    path('vehicle-types', views.VehicleTypeList.as_view()),
    path('vehicle-types/<int:pk>', views.VehicleTypeDetails.as_view()),
    path('vehicles', views.VehicleList.as_view()),
    path('vehicles/<int:pk>', views.VehicleDetails.as_view()),

    path('staff-types', views.StaffTypeList.as_view()),
    path('staff-types/<int:pk>', views.StaffTypeDetails.as_view()),
    path('staffs', views.StaffList.as_view()),
    path('staffs/<int:pk>', views.StaffDetails.as_view()),

    path('scenario-types', views.ScenarioTypeList.as_view()),
    path('scenario-types/<int:pk>', views.ScenarioTypeDetails.as_view()),
    path('scenarios', views.ScenarioList.as_view()),
    path('scenarios/<int:pk>', views.ScenarioDetails.as_view()),

    path('calls', views.CallList.as_view()),
    path('calls/<int:pk>', views.CallDetails.as_view()),
    path('calls/<int:pk>/ressources', views.CallDetailsWithRessources.as_view()),


]
