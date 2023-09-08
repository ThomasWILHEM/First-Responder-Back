from sqlalchemy.orm import Session
from ..models import vehicle
from ..schemas import vehicle as schemas
from . import crud_vehicle, crud_call, crud_building


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


def add_vehicle_to_building(db: Session, vehicle_id: int, building_id: int):
    vehicle_instance = get_vehicle(db, vehicle_id)
    building_instance = crud_building.get_building(db, building_id)

    if not vehicle_instance:
        raise ValueError("Vehicle not found")
    if not building_instance:
        raise ValueError("Building not found")

    building_instance.vehicles.append(vehicle_instance)
    vehicle_instance.building = building_instance

    db.commit()
    return building_instance


def send_to_call(db: Session, call_id: int, vehicle_id: int):
    call_instance = crud_call.get_call(db, call_id)
    vehicle_instance = crud_vehicle.get_vehicle(db, vehicle_id)

    if not call_instance:
        raise ValueError("Call not found")
    if not vehicle_instance:
        raise ValueError("Vehicle not found")

    call_instance.vehicles.append(vehicle_instance)
    vehicle_instance.call = call_instance

    db.commit()
    return call_instance
