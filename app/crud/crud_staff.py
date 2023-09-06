from sqlalchemy.orm import Session
from ..models import staff
from ..schemas import staff as schemas


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
