from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_building, crud_building_type
from ..schemas import building as schemas

router = APIRouter(
    prefix="/buildings",
    tags=["buildings"],
    responses={404: {"description": "Not found"}},
)


def get_building_by_id(db: Session = Depends(get_db), building_id: int = Path(...)):
    db_building = crud_building.get_building(db, building_id)
    if db_building is None:
        raise HTTPException(status_code=404, detail="Building not found")
    return db_building


@router.get("/", response_model=schemas.AllBuildings)
def read_all_buildings(db: Session = Depends(get_db)):
    buildings = crud_building.get_all_buildings(db)
    return {"results": buildings}


@router.post("/", response_model=schemas.Building)
def create_building(building_create: schemas.BuildingCreate, db: Session = Depends(get_db)):
    type = crud_building_type.get_building_type(db, building_create.type_id)
    if type is None:
        raise HTTPException(status_code=404, detail="Building type not found")
    return crud_building.create_building(db, building_create)


@router.get("/{building_id}", response_model=schemas.Building)
def read_building(building: schemas.Building = Depends(get_building_by_id)):
    return building


@router.delete("/{building_id}")
def delete_building(db: Session = Depends(get_db), building: schemas.Building = Depends(get_building_by_id)):
    crud_building.delete_building(db, building)
    return {"message": "Building deleted"}
