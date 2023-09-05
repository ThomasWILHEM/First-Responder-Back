from pydantic import BaseModel


class VehicleTypeCreate(BaseModel):
    name: str


class VehicleType(VehicleTypeCreate):
    id: int


class VehicleTypeUpdate(BaseModel):
    name: str


class VehicleTypeDelete(BaseModel):
    id: int


class AllVehicleTypes(BaseModel):
    results: list[VehicleType]
