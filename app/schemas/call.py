from pydantic import BaseModel
from datetime import datetime
from .scenario import Scenario


class CallCreate(BaseModel):
    coordinates_latitude: float
    coordinates_longitude: float
    datetime: datetime
    completion_datetime: datetime
    scenario_id: int
    mission_status: str


class Call(CallCreate):
    id: int
    scenario: Scenario


class AllCalls(BaseModel):
    results: list[Call]