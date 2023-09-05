from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_vehicle_type
from ..schemas import vehicle_type as schemas

router = APIRouter(prefix="/vehicles-types",
    tags=["vehicles-types"],
    responses={404: {"description": "Not found"}},
)


def get_vehicle_type_by_id(db: Session = Depends(get_db), vehicle_type_id: int = Path(...)):
    db_vehicle_type = crud_vehicle_type.get_vehicle_type(db, vehicle_type_id)
    if db_vehicle_type is None:
        raise HTTPException(status_code=404, detail="VehicleType not found")
    return db_vehicle_type


@router.get("/", response_model=schemas.AllVehicleTypes)
def read_all_vehicle_types(db: Session = Depends(get_db)):
    vehicle_types = crud_vehicle_type.get_all_vehicle_types(db)
    return {"results": vehicle_types}


@router.post("/", response_model=schemas.VehicleType)
def create_vehicle_type(vehicle_type: schemas.VehicleTypeCreate, db: Session = Depends(get_db)):
    return crud_vehicle_type.create_vehicle_type(db, vehicle_type)


@router.get("/{vehicle_type_id}", response_model=schemas.VehicleType)
def read_vehicle_type(vehicle_type: schemas.VehicleType = Depends(get_vehicle_type_by_id)):
    return vehicle_type


@router.delete("/{type_id}", response_model=schemas.VehicleType)
def delete_vehicle_type(type_id: int, db: Session = Depends(get_db)):
    vehicle_type = crud_vehicle_type.get_vehicle_type(db, type_id)
    if vehicle_type is None:
        raise HTTPException(status_code=404, detail="Vehicle Type not found")
    return crud_vehicle_type.delete_vehicle_type(db, vehicle_type)