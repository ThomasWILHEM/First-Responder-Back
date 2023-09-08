from pydantic import BaseModel


class BuildingTypeCreate(BaseModel):
    name: str


class BuildingType(BuildingTypeCreate):
    id: int


class BuildingTypeUpdate(BaseModel):
    name: str


class BuildingTypeDelete(BaseModel):
    id: int


class AllBuildingTypes(BaseModel):
    results: list[BuildingType]
