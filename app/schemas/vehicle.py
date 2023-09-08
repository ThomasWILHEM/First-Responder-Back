from pydantic import BaseModel
from .vehicle_type import VehicleType
from .call import Call
from typing import Optional


class VehicleCreate(BaseModel):
    coordinates_latitude: float
    coordinates_longitude: float
    type_id: int
    call_id: Optional[int] = None


class Vehicle(VehicleCreate):
    id: int
    type: VehicleType
    call: Optional[Call] = None


class VehicleUpdate(BaseModel):
    coordinates_latitude: float
    coordinates_longitude: float


class VehicleDelete(VehicleCreate):
    id: int


class AllVehicles(BaseModel):
    results: list[Vehicle]
