from sqlalchemy.orm import Session
from ..models import building
from ..schemas import building as schemas


def get_all_buildings(db: Session, skip: int = 0, limit: int = 100):
    return (db.query(building.Building)
            .order_by(building.Building.id.asc())
            .offset(skip).limit(limit).all())


def get_building(db: Session, building_id: int):
    return db.query(building.Building).filter(building.Building.id == building_id).first()


def create_building(db: Session, building_create: schemas.BuildingCreate):
    db_building = building.Building(**building_create.dict())
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    return db_building


def delete_building(db: Session, building: building.Building):
    db.delete(building)
    db.commit()
