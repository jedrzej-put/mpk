from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..package.database import crud, models, schemas
from ..dependencies import get_db
from ..request_models import StopRequest, StopRequestExtend
from ..package.classes.StopsController import StopsController
from ..package.classes.StopTimesController import StopTimesController

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

@router.get("/stop_times/{stop_id}", response_model=list[schemas.StopTime])
def read_stops_times(stop_id: str, db: Session = Depends(get_db)):
    stop_times = crud.get_stop_times_by_stop_id(db, stop_id=stop_id)
    print(stop_times[0])
    return stop_times

# @router.get("/stop_times/nearest", response_model=list[schemas.StopTime])
@router.get("/departures")
def read_stops_departures(req: StopRequestExtend):
    departures = StopTimesController(req.lat, req.lon, req.age, req.target_lat, req.target_lon).get_departures_from_stop_to_process()
    
    return departures