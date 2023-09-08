from sqlalchemy.orm import Session
from ..models import vehicle_type
from ..schemas import vehicle_type as schemas


def get_all_vehicle_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(vehicle_type.VehicleType).offset(skip).limit(limit).all()


def create_vehicle_type(db: Session, vehicle_type_create: schemas.VehicleType):
    db_vehicle_type = vehicle_type.VehicleType(**vehicle_type_create.dict())
    db.add(db_vehicle_type)
    db.commit()
    db.refresh(db_vehicle_type)
    return db_vehicle_type


def get_vehicle_type(db: Session, vehicle_type_id: int):
    return db.query(vehicle_type.VehicleType).filter(vehicle_type.VehicleType.id == vehicle_type_id).first()


def delete_vehicle_type(db: Session, vehicle_type: vehicle_type.VehicleType):
    db.delete(vehicle_type)
    db.commit()
    return vehicle_type
