from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_staff, crud_staff_type
from ..schemas import staff as schemas

router = APIRouter(
    prefix="/staffs",
    tags=["staffs"],
    responses={404: {"description": "Not found"}},
)


def get_staff_by_id(db: Session = Depends(get_db), staff_id: int = Path(...)):
    db_staff = crud_staff.get_staff(db, staff_id)
    if db_staff is None:
        raise HTTPException(status_code=404, detail="Staff not found")
    return db_staff


@router.get("/", response_model=schemas.AllStaffs)
def read_all_staffs(db: Session = Depends(get_db)):
    staffs = crud_staff.get_all_staffs(db)
    return {"results": staffs}


@router.post("/", response_model=schemas.Staff)
def create_staff(staff_create: schemas.StaffCreate, db: Session = Depends(get_db)):
    type = crud_staff_type.get_staff_type(db, staff_create.type_id)
    if type is None:
        raise HTTPException(status_code=404, detail="Staff type not found")
    return crud_staff.create_staff(db, staff_create)


@router.get("/{staff_id}", response_model=schemas.Staff)
def read_staff(staff: schemas.Staff = Depends(get_staff_by_id)):
    return staff


@router.delete("/{staff_id}")
def delete_staff(db: Session = Depends(get_db), staff: schemas.Staff = Depends(get_staff_by_id)):
    crud_staff.delete_staff(db, staff)
    return {"message": "Staff deleted"}


@router.post("/add_to_vehicle", response_model=schemas.Vehicle)
def add_staff_to_vehicle(
    staff_id: int,
    vehicle_id: int,
    db: Session = Depends(get_db),
):
    updated_vehicle = crud_staff.add_staff_to_vehicle(db, staff_id, vehicle_id)

    if not updated_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return updated_vehicle
