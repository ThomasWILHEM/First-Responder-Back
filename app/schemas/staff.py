from pydantic import BaseModel
from typing import Optional
from .staff_type import StaffType
from .vehicle import Vehicle


class StaffCreate(BaseModel):
    firstname: str
    lastname: str
    type_id: int
    vehicle_id: Optional[int] = None


class Staff(StaffCreate):
    id: int
    type: StaffType
    vehicle: Optional[Vehicle]


class StaffUpdate(BaseModel):
    firstname: str
    lastname: str


class StaffAddVehicle(BaseModel):
    vehicle_id: int


class StaffDelete(StaffCreate):
    id: int


class AllStaffs(BaseModel):
    results: list[Staff]
