from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_vehicle, crud_vehicle_type
from ..schemas import vehicle as schemas
from ..schemas import call

router = APIRouter(
    prefix="/vehicles",
    tags=["vehicles"],
    responses={404: {"description": "Not found"}},
)


def get_vehicle_by_id(db: Session = Depends(get_db), vehicle_id: int = Path(...)):
    db_vehicle = crud_vehicle.get_vehicle(db, vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle


@router.get("/", response_model=schemas.AllVehicles)
def read_all_vehicles(db: Session = Depends(get_db)):
    vehicles = crud_vehicle.get_all_vehicles(db)
    return {"results": vehicles}


@router.post("/", response_model=schemas.Vehicle)
def create_vehicle(vehicle_create: schemas.VehicleCreate, db: Session = Depends(get_db)):
    type = crud_vehicle_type.get_vehicle_type(db, vehicle_create.type_id)
    if type is None:
        raise HTTPException(status_code=404, detail="Vehicle type not found")
    return crud_vehicle.create_vehicle(db, vehicle_create)


@router.get("/{vehicle_id}", response_model=schemas.Vehicle)
def read_vehicle(vehicle: schemas.Vehicle = Depends(get_vehicle_by_id)):
    return vehicle


@router.delete("/{vehicle_id}")
def delete_vehicle(db: Session = Depends(get_db), vehicle: schemas.Vehicle = Depends(get_vehicle_by_id)):
    crud_vehicle.delete_vehicle(db, vehicle)
    return {"message": "Vehicle deleted"}


@router.post("/add_to_building", response_model=schemas.Vehicle)
def add_vehicle_to_building(
    vehicle_id: int,
    building_id: int,
    db: Session = Depends(get_db)):

    updated_building = crud_vehicle.add_vehicle_to_building(db, vehicle_id, building_id)

    if not updated_building:
        raise HTTPException(status_code=404, detail="Building not found")

    return updated_building

@router.post("/send_to_call", response_model=call.Call)
def send_vehicle_to_call(
    vehicle_id: int,
    call_id: int,
    db: Session = Depends(get_db)):

    updated_call = crud_vehicle.send_to_call(db, call_id, vehicle_id)

    if not updated_call:
        raise HTTPException(status_code=404, detail="Call not found")

    return updated_call

