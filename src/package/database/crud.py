from sqlalchemy.orm import Session
from datetime import timedelta
from . import models, schemas
from typing import Dict


def get_routes(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.Route).offset(skip).limit(limit).all()]


def get_cities(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.City).offset(skip).limit(limit).all()]


def get_trips(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.Trip).offset(skip).limit(limit).all()]


def get_calendars(db: Session, skip: int = 0, limit: int = 1000000):
    return [
        _.toDict() for _ in db.query(models.Calendar).offset(skip).limit(limit).all()
    ]


def get_stops(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.Stop).offset(skip).limit(limit).all()]


def get_stop_times_by_stop_id(db: Session, stop_id: str):
    return [
        _.toDict()
        for _ in db.query(models.StopTime)
        .filter(models.StopTime.stop_id == stop_id)
        .all()
    ]


def get_trip_by_trip_id(db: Session, trip_id):
    return db.query(models.Trip).filter(models.Trip.trip_id == trip_id).first().toDict()


def get_calendar_by_service_id(db: Session, service_id):
    return (
        db.query(models.Calendar)
        .filter(models.Calendar.service_id == service_id)
        .first()
        .toDict()
    )

def get_stop_by_auto_increment_id(db: Session, auto_increment_id):
    return db.query(models.StopTime).filter(models.StopTime.auto_increment_id == auto_increment_id).first().toDict()

def get_calendar_by_stop_time(db: Session, stop_time: Dict):
    trip = get_trip_by_trip_id(db, stop_time.get("trip_id"))
    return get_calendar_by_service_id(db, trip.get("service_id"))