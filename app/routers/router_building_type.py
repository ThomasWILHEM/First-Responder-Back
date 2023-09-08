from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_building_type
from ..schemas import building_type as schemas

router = APIRouter(prefix="/buildings-types",
    tags=["buildings-types"],
    responses={404: {"description": "Not found"}},
)


def get_building_type_by_id(db: Session = Depends(get_db), building_type_id: int = Path(...)):
    db_building_type = crud_building_type.get_building_type(db, building_type_id)
    if db_building_type is None:
        raise HTTPException(status_code=404, detail="BuildingType not found")
    return db_building_type


@router.get("/", response_model=schemas.AllBuildingTypes)
def read_all_building_types(db: Session = Depends(get_db)):
    building_types = crud_building_type.get_all_building_types(db)
    return {"results": building_types}


@router.post("/", response_model=schemas.BuildingType)
def create_building_type(building_type: schemas.BuildingTypeCreate, db: Session = Depends(get_db)):
    return crud_building_type.create_building_type(db, building_type)


@router.get("/{building_type_id}", response_model=schemas.BuildingType)
def read_building_type(building_type: schemas.BuildingType = Depends(get_building_type_by_id)):
    return building_type


@router.delete("/{type_id}", response_model=schemas.BuildingType)
def delete_building_type(type_id: int, db: Session = Depends(get_db)):
    building_type = crud_building_type.get_building_type(db, type_id)
    if building_type is None:
        raise HTTPException(status_code=404, detail="Building Type not found")
    return crud_building_type.delete_building_type(db, building_type)