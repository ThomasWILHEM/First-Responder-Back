from pydantic import BaseModel, HttpUrl

class Scenario_Type(BaseModel):
    id: int
    name: str
    