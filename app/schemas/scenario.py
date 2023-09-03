from pydantic import BaseModel
from .scenario_type import Scenario_Type

class Scenario(BaseModel):
    id: int
    name: str
    description: str
    type: Scenario_Type

class AllScenarios(BaseModel):
    results: list[Scenario]
