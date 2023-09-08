from sqlalchemy.orm import Session
from ..models import building_type
from ..schemas import building_type as schemas


def get_all_building_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(building_type.BuildingType).offset(skip).limit(limit).all()


def create_building_type(db: Session, building_type_create: schemas.BuildingType):
    db_building_type = building_type.BuildingType(**building_type_create.dict())
    db.add(db_building_type)
    db.commit()
    db.refresh(db_building_type)
    return db_building_type


def get_building_type(db: Session, building_type_id: int):
    return db.query(building_type.BuildingType).filter(building_type.BuildingType.id == building_type_id).first()


def delete_building_type(db: Session, building_type: building_type.BuildingType):
    db.delete(building_type)
    db.commit()
    return building_type