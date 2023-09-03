from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_scenario
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

@router.post("/scenarios/", response_model=schemas.Scenario)
def create_scenario(scenario_create: schemas.ScenarioCreate, db: Session = Depends(get_db)):
    return crud_scenario.create_scenario(db, scenario_create)

@router.get("/scenarios/{scenario_id}", response_model=schemas.Scenario)
def read_scenario(scenario: schemas.Scenario = Depends(get_scenario_by_id)):
    return scenario