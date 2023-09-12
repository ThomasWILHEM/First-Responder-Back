from pydantic import BaseModel
from .building_type import BuildingType


class BuildingCreate(BaseModel):
    name: str
    coordinates_latitude: float
    coordinates_longitude: float
    type_id: int


class Building(BuildingCreate):
    id: int
    type: BuildingType


class BuildingUpdate(BaseModel):
    coordinates_latitude: float
    coordinates_longitude: float


class BuildingDelete(BuildingCreate):
    id: int


class AllBuildings(BaseModel):
    results: list[Building]
