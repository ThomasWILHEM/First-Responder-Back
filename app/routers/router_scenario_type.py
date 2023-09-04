from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_scenario_type
from ..schemas import scenario_type as schemas

router = APIRouter(prefix="/scenarios-types",
    tags=["scenarios-types"],
    responses={404: {"description": "Not found"}},
)


def get_scenario_type_by_id(db: Session = Depends(get_db), scenario_type_id: int = Path(...)):
    db_scenario_type = crud_scenario_type.get_scenario_type(db, scenario_type_id)
    if db_scenario_type is None:
        raise HTTPException(status_code=404, detail="ScenarioType not found")
    return db_scenario_type


@router.post("/", response_model=schemas.ScenarioType)
def create_scenario_type(scenario_type: schemas.ScenarioTypeCreate, db: Session = Depends(get_db)):
    return crud_scenario_type.create_scenario_type(db, scenario_type)


@router.get("/{scenario_type_id}", response_model=schemas.ScenarioType)
def read_scenario_type(scenario_type: schemas.ScenarioType = Depends(get_scenario_type_by_id)):
    return scenario_type


@router.delete("/{type_id}", response_model=schemas.ScenarioType)
def delete_scenario_type(type_id: int, db: Session = Depends(get_db)):
    scenario_type = crud_scenario_type.get_scenario_type(db, type_id)
    if scenario_type is None:
        raise HTTPException(status_code=404, detail="Scenario Type not found")
    return crud_scenario_type.delete_scenario_type(db, scenario_type)