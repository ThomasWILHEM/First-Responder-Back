from sqlalchemy.orm import Session
from ..models import staff, vehicle
from ..schemas import staff as schemas
from .crud_vehicle import get_vehicle


def get_all_staffs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(staff.Staff).offset(skip).limit(limit).all()


def get_staff(db: Session, staff_id: int):
    return db.query(staff.Staff).filter(staff.Staff.id == staff_id).first()


def create_staff(db: Session, staff_create: schemas.StaffCreate):
    db_staff = staff.Staff(**staff_create.dict())
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff


def delete_staff(db: Session, staff: staff.Staff):
    db.delete(staff)
    db.commit()


def add_staff_to_vehicle(db: Session, staff_id: int, vehicle_id: int):
    staff_instance = get_staff(db, staff_id)
    vehicle_instance = get_vehicle(db, vehicle_id)

    if not staff_instance:
        raise ValueError("Staff not found")
    if not vehicle_instance:
        raise ValueError("Vehicle not found")

    vehicle_instance.occupants.append(staff_instance)
    staff_instance.vehicle = vehicle_instance

    db.commit()
    return vehicle_instance
