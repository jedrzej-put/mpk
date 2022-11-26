from ..database import crud
from ..database.models import Route, City
from ..database.Model import Model
from ...dependencies import get_db
from sqlalchemy.orm import Session
from decimal import *
from math import sin, cos, sqrt, atan2, radians
from typing import List, Dict

class StopsController():
    def __init__(self):
        self.all_stops:List[Dict] = crud.get_stops(db=next(get_db()))
    
    @staticmethod
    def calc_distance(lat1: str, lon1: str, lat2: str, lon2: str) -> float:
        _R = 6373.0 * 10e3
        _lat1, _lat2, _lon1, _lon2 = radians(Decimal(lat1)), radians(Decimal(lat2)), radians(Decimal(lon1)), radians(Decimal(lon2))
        _d_lon = _lon2 - _lon1
        _d_lat = _lat2 - _lat1

        a = sin(_d_lat / 2)**2 + cos(_lat1) * cos(_lat2) * sin(_d_lon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return _R * c
    
    def nearest_stops_to_up(self, lat:str, lon:str, count:int = 5, stops:List[Dict] = None) -> List[Dict]:
        _stops = self.all_stops if stops is None else stops
        
        # key(stop_id): value(distance between stop_id and point(lat, lon))
        distances = {stop.get('stop_id'):self.calc_distance(lat, lon, stop.get('stop_lat'), stop.get('stop_lon') ) for stop in _stops}
        
        ordered_stops = sorted(_stops, key=lambda stop: distances.get(stop.get('stop_id'))) 
        return ordered_stops[:count]