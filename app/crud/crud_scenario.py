from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
from ..models import scenario
from ..schemas import scenario as schemas

def get_all_scenarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(scenario.Scenario).offset(skip).limit(limit).all()

def get_scenario(db: Session, scenario_id: int):
    return db.query( scenario.Scenario).filter(scenario.Scenario.id == scenario_id).first()

def create_scenario(db: Session, scenario_create: schemas.ScenarioCreate):
    db_scenario = scenario.Scenario(**scenario_create.dict())
    db.add(db_scenario)
    db.commit()
    db.refresh(db_scenario)
    return db_scenario