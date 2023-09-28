from pydantic import BaseModel, Field
from .vehicle_type import VehicleType
from .building import Building
from typing import Optional
from .call import Call

class VehicleCreate(BaseModel):
    coordinates_latitude: float
    coordinates_longitude: float
    type_id: int
    call_id: Optional[int] = None
    building_id: Optional[int] = None


class Vehicle(VehicleCreate):
    id: int
    type: VehicleType
    call: Optional[Call] = None
    building: Optional[Building] = None


class VehicleUpdate(BaseModel):
    coordinates_latitude: float
    coordinates_longitude: float


class VehicleDelete(VehicleCreate):
    id: int


class ListVehicle(BaseModel):
    vehicles: list[int]


class AllVehicles(BaseModel):
    results: list[Vehicle]
