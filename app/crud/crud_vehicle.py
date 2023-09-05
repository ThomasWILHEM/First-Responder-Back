from sqlalchemy.orm import Session
from ..models import vehicle
from ..schemas import vehicle as schemas


def get_all_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(vehicle.Vehicle).offset(skip).limit(limit).all()


def get_vehicle(db: Session, vehicle_id: int):
    return db.query(vehicle.Vehicle).filter(vehicle.Vehicle.id == vehicle_id).first()


def create_vehicle(db: Session, vehicle_create: schemas.VehicleCreate):
    db_vehicle = vehicle.Vehicle(**vehicle_create.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def delete_vehicle(db: Session, vehicle: vehicle.Vehicle):
    db.delete(vehicle)
    db.commit()
