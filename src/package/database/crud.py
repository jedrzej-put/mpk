from sqlalchemy.orm import Session
from datetime import timedelta
from . import models, schemas


def get_routes(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.Route).offset(skip).limit(limit).all()]

def get_cities(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.City).offset(skip).limit(limit).all()] 

def get_trips(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.Trip).offset(skip).limit(limit).all()]

def get_stops(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.Stop).offset(skip).limit(limit).all()] 

def get_stop_times_by_stop_id(db: Session, stop_id: str):
    return [_.toDict() for _ in db.query(models.StopTime).filter(models.StopTime.stop_id == stop_id).all()]
