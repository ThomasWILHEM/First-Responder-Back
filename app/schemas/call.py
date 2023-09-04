from pydantic import BaseModel
from typing import Tuple
from datetime import datetime
from .scenario import Scenario


class CallCreate(BaseModel):
    coordinates: Tuple[float, float]
    timestamp: datetime
    completion_timestamp: datetime
    scenario_id: int
    mission_status: str


class Call(CallCreate):
    id: int
    scenario: Scenario

class AllCalls(BaseModel):
    results: list[Call]