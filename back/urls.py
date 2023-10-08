from django.urls import path
from . import views

urlpatterns = [
    path('building-types', views.BuildingTypeList.as_view()),
    path('building-types/<int:pk>', views.BuildingTypeDetails.as_view()),
    path('buildings', views.BuildingList.as_view()),
    path('buildings/<int:pk>', views.BuildingDetails.as_view()),

]
