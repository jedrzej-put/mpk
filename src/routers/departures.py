from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..package.database import crud, models, schemas
from ..dependencies import get_db


router = APIRouter(
    tags=["departures"],
)

@router.get("/stops/", response_model=list[schemas.Stop])
def read_stops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stops = crud.get_stops(db, skip=skip, limit=limit)
    return stops


@router.get("/departures/", response_model=list[schemas.City])
def read_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cities = crud.get_cities(db, skip=skip, limit=limit)
    return cities

