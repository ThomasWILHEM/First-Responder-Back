from sqlalchemy.orm import Session
from ..models import call
from ..schemas import call as schemas


def get_all_calls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(call.Call).offset(skip).limit(limit).all()


def get_call(db: Session, call_id: int):
    return db.query(call.Call).filter(call.Call.id == call_id).first()


def create_call(db: Session, call_create: schemas.CallCreate):
    db_call = call.Call(**call_create.dict())
    db.add(db_call)
    db.commit()
    db.refresh(db_call)
    return db_call


def delete_call(db: Session, call: call.Call):
    db.delete(call)
    db.commit()
