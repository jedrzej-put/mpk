from ..database import crud
from ..database.models import Route, City
from ..database.Model import Model
from ...dependencies import get_db
from sqlalchemy.orm import Session
from decimal import *
from math import sin, cos, sqrt, atan2, radians

class StopsController():
    def __init__(self):
        self.all_stops = crud.get_stops(db=next(get_db()))
    
    @staticmethod
    def calc_distance(lat1: str, lon1: str, lat2: str, lon2: str) -> float:
        _R = 6373.0
        _lat1, _lat2, _lon1, _lon2 = radians(Decimal(lat1)), radians(Decimal(lat2)), radians(Decimal(lon1)), radians(Decimal(lon2))
        _d_lon = _lon2 - _lon1
        _d_lat = _lat2 - _lat1

        a = sin(_d_lat / 2)**2 + cos(_lat1) * cos(_lat2) * sin(_d_lon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return _R * c