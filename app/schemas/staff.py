from pydantic import BaseModel
from .staff_type import StaffType


class StaffCreate(BaseModel):
    firstname: str
    lastname: str
    type_id: int


class Staff(StaffCreate):
    id: int
    type: StaffType


class StaffUpdate(BaseModel):
    firstname: str
    lastname: str


class StaffDelete(StaffCreate):
    id: int


class AllStaffs(BaseModel):
    results: list[Staff]
