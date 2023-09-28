from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_ressources, crud_vehicle
from ..schemas import building as schemas
from.router_call import get_call_by_id

router = APIRouter(
    prefix="/ressources",
    tags=["ressources"],
    responses={404: {"description": "Not found"}},
)


@router.get("/call/{call_id}")
def get_call_ressources(call_id: int, db: Session = Depends(get_db)):
    db_call = get_call_by_id(db, call_id)
    if db_call is None:
        raise HTTPException(status_code=404, detail="Call not found")
    vehicles_on_scene = crud_ressources.get_vehicles_on_scene(db, call_id)
    all_vehicles = crud_vehicle.get_all_vehicles(db, get_type=True)
    available_vehicles = [vehicule for vehicule in all_vehicles if vehicule.id not in [v.id for v in vehicles_on_scene]]

    return {
        "vehiclesOnScene": vehicles_on_scene,
        "availableVehicles": available_vehicles
    }
