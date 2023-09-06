from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_staff_type
from ..schemas import staff_type as schemas

router = APIRouter(prefix="/staffs-types",
    tags=["staffs-types"],
    responses={404: {"description": "Not found"}},
)


def get_staff_type_by_id(db: Session = Depends(get_db), staff_type_id: int = Path(...)):
    db_staff_type = crud_staff_type.get_staff_type(db, staff_type_id)
    if db_staff_type is None:
        raise HTTPException(status_code=404, detail="StaffType not found")
    return db_staff_type


@router.get("/", response_model=schemas.AllStaffTypes)
def read_all_staff_types(db: Session = Depends(get_db)):
    staff_types = crud_staff_type.get_all_staff_types(db)
    return {"results": staff_types}


@router.post("/", response_model=schemas.StaffType)
def create_staff_type(staff_type: schemas.StaffTypeCreate, db: Session = Depends(get_db)):
    return crud_staff_type.create_staff_type(db, staff_type)


@router.get("/{staff_type_id}", response_model=schemas.StaffType)
def read_staff_type(staff_type: schemas.StaffType = Depends(get_staff_type_by_id)):
    return staff_type


@router.delete("/{type_id}", response_model=schemas.StaffType)
def delete_staff_type(type_id: int, db: Session = Depends(get_db)):
    staff_type = crud_staff_type.get_staff_type(db, type_id)
    if staff_type is None:
        raise HTTPException(status_code=404, detail="Staff Type not found")
    return crud_staff_type.delete_staff_type(db, staff_type)
