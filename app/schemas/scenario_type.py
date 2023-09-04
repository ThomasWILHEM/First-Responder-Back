from pydantic import BaseModel


class ScenarioTypeCreate(BaseModel):
    name: str


class ScenarioType(ScenarioTypeCreate):
    id: int


class ScenarioTypeUpdate(BaseModel):
    name: str


class ScenarioTypeDelete(BaseModel):
    id: int


class AllScenarioTypes(BaseModel):
    results: list[ScenarioType]
