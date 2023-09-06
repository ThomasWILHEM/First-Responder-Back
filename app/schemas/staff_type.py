from pydantic import BaseModel


class StaffTypeCreate(BaseModel):
    name: str


class StaffType(StaffTypeCreate):
    id: int


class StaffTypeUpdate(BaseModel):
    name: str


class StaffTypeDelete(BaseModel):
    id: int


class AllStaffTypes(BaseModel):
    results: list[StaffType]
