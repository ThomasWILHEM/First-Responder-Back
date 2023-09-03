from fastapi import APIRouter
from app.schemas.scenario import Scenario, AllScenarios

router = APIRouter(
    prefix="/scenarios",
    tags=["scenarios"],
    responses={404: {"description": "Not found"}},
)

SCENARIO = [
    {
        "id": 1,
        "name": "Accident",
        "description": "Serious Eats",
        "type": {
            "id": 1,
            "name": "Pompier"
        }
    },
    {
        "id": 2,
        "name": "Vol",
        "description": "No Recipes",
        "type": {
            "id": 1,
            "name": "Police"
        }
    }
]


@router.get('/', response_model=AllScenarios)
async def read_scenarios():
    return {"results": [Scenario(**scenario) for scenario in SCENARIO]}


@router.get('/{scenario_id}', response_model=Scenario)
async def read_scenarios_by_id(scenario_id: int):
    scenario = [scenario for scenario in SCENARIO if scenario["id"] == scenario_id]
    if scenario:
        return scenario[0]