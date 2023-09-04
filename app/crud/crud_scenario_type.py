from sqlalchemy.orm import Session
from ..models import scenario_type
from ..schemas import scenario_type as schemas


def create_scenario_type(db: Session, scenario_type_create: schemas.ScenarioTypeCreate):
    db_scenario_type = scenario_type.ScenarioType(**scenario_type_create.dict())
    db.add(db_scenario_type)
    db.commit()
    db.refresh(db_scenario_type)
    return db_scenario_type


def get_scenario_type(db: Session, scenario_type_id: int):
    return db.query(scenario_type.ScenarioType).filter(scenario_type.ScenarioType.id == scenario_type_id).first()


def delete_scenario_type(db: Session, scenario_type: scenario_type.ScenarioType):
    db.delete(scenario_type)
    db.commit()
    return scenario_type