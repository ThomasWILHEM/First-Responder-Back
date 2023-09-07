from pydantic import BaseModel
from .vehicle_type import VehicleType


class VehicleCreate(BaseModel):
    coordinates_latitude: float
    coordinates_longitude: float
    type_id: int


class Vehicle(VehicleCreate):
    id: int
    type: VehicleType


class VehicleUpdate(BaseModel):
    coordinates_latitude: float
    coordinates_longitude: float


class VehicleDelete(VehicleCreate):
    id: int


class AllVehicles(BaseModel):
    results: list[Vehicle]
