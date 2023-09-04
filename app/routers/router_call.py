from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..crud import crud_call
from ..schemas import call as schemas

router = APIRouter(
    prefix="/calls",
    tags=["calls"],
    responses={404: {"description": "Not found"}},
)


def get_call_by_id(db: Session = Depends(get_db), call_id: int = Path(...)):
    db_call = crud_call.get_call(db, call_id)
    if db_call is None:
        raise HTTPException(status_code=404, detail="Call not found")
    return db_call


@router.get("/", response_model=schemas.AllCalls)
def read_all_calls(db: Session = Depends(get_db)):
    calls = crud_call.get_all_calls(db)
    return {"results": calls}


