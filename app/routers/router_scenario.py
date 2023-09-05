from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_scenario, crud_scenario_type
from ..schemas import scenario as schemas

router = APIRouter(
    prefix="/scenarios",
    tags=["scenarios"],
    responses={404: {"description": "Not found"}},
)


def get_scenario_by_id(db: Session = Depends(get_db), scenario_id: int = Path(...)):
    db_scenario = crud_scenario.get_scenario(db, scenario_id)
    if db_scenario is None:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return db_scenario


@router.get("/", response_model=schemas.AllScenarios)
def read_all_scenarios(db: Session = Depends(get_db)):
    scenarios = crud_scenario.get_all_scenarios(db)
    return {"results": scenarios}


@router.post("/", response_model=schemas.Scenario)
def create_scenario(scenario_create: schemas.ScenarioCreate, db: Session = Depends(get_db)):
    type = crud_scenario_type.get_scenario_type(db, scenario_create.type_id)
    if type is None:
        raise HTTPException(status_code=404, detail="Scenario type not found")
    return crud_scenario.create_scenario(db, scenario_create)


@router.get("/{scenario_id}", response_model=schemas.Scenario)
def read_scenario(scenario: schemas.Scenario = Depends(get_scenario_by_id)):
    return scenario


@router.delete("/{scenario_id}")
def delete_scenario(db: Session = Depends(get_db), scenario: schemas.Scenario = Depends(get_scenario_by_id)):
    crud_scenario.delete_scenario(db, scenario)
    return {"message": "Scenario deleted"}
