from sqlalchemy.orm import Session

from . import models, schemas


def get_routes(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.Route).offset(skip).limit(limit).all()]

def get_cities(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.City).offset(skip).limit(limit).all()] 

def get_trips(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.Trip).offset(skip).limit(limit).all()]

def get_stops(db: Session, skip: int = 0, limit: int = 1000000):
    return [_.toDict() for _ in db.query(models.Stop).offset(skip).limit(limit).all()] 