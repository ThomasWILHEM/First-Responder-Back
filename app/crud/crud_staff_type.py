from sqlalchemy.orm import Session
from ..models import staff_type
from ..schemas import staff_type as schemas


def get_all_staff_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(staff_type.StaffType).offset(skip).limit(limit).all()


def create_staff_type(db: Session, staff_type_create: schemas.StaffType):
    db_staff_type = staff_type.StaffType(**staff_type_create.dict())
    db.add(db_staff_type)
    db.commit()
    db.refresh(db_staff_type)
    return db_staff_type


def get_staff_type(db: Session, staff_type_id: int):
    return db.query(staff_type.StaffType).filter(staff_type.StaffType.id == staff_type_id).first()


def delete_staff_type(db: Session, staff_type: staff_type.StaffType):
    db.delete(staff_type)
    db.commit()
    return staff_type