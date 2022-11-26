from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..package.database import crud, models, schemas
from ..dependencies import get_db


router = APIRouter(
    tags=["city_route"],
)

@router.get("/cities/", response_model=list[schemas.City])
def read_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cities = crud.get_cities(db, skip=skip, limit=limit)
    return cities

@router.get("/routes/", response_model=list[schemas.Route])
def read_routes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    routes = crud.get_routes(db, skip=skip, limit=limit)
    return routes