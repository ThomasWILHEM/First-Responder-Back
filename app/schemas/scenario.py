from pydantic import BaseModel
from .scenario_type import ScenarioType

class ScenarioCreate(BaseModel):
    name: str
    description: str
    type_id: int

class Scenario(ScenarioCreate):
    id: int
    type: ScenarioType

class ScenarioUpdate(BaseModel):
    name: str
    description: str
    type_id: int

class ScenarioDelete(ScenarioCreate):
    id: int

class AllScenarios(BaseModel):
    results: list[Scenario]