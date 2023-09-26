from sqlalchemy.orm import Session
from ..models import vehicle

def get_vehicles_on_scene(db: Session, call_id: int):
    return db.query(vehicle.Vehicle).filter(vehicle.Vehicle.call_id == call_id).all()


