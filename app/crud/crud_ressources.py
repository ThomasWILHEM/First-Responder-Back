from sqlalchemy.orm import Session
from ..models.vehicle import Vehicle


def get_vehicles_on_scene(db: Session, call_id: int):
    vehicles = db.query(Vehicle).filter(Vehicle.call_id == call_id).all()

    for vehicle in vehicles:
        db.refresh(vehicle.type)

    return vehicles


