from sqlalchemy.orm import Session

from . import models, schemas


def get_routes(db: Session, skip: int = 0, limit: int = 100):
    return [_.toDict() for _ in db.query(models.Route).offset(skip).limit(limit).all()]

def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return [_.toDict() for _ in db.query(models.City).offset(skip).limit(limit).all()] 
