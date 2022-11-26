from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..package.database import crud, models, schemas
from ..dependencies import get_db
from ..request_models import StopRequest
from ..package.classes.StopsController import StopsController

router = APIRouter(
    tags=["departures"],
)

stops_controller = StopsController()

@router.get("/stops/", response_model=list[schemas.Stop])
def read_stops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stops = crud.get_stops(db, skip=skip, limit=limit)
    return stops


@router.get("/stops/nearest", response_model=list[schemas.Stop])
def read_cities(req: StopRequest):
    stops = stops_controller.nearest_stops_to_up(req.lat, req.lon, req.age, req.count)
    return stops
