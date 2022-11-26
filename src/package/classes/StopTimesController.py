from ..database import crud
from ..database.models import Route, City
from ..database.Model import Model
from ...dependencies import get_db
from sqlalchemy.orm import Session
from decimal import *
from math import sin, cos, sqrt, atan2, radians
from typing import List, Dict
from toolz.functoolz import compose
from datetime import datetime, timedelta, time, date

class StopTimesController:
    def __init__(self):
        self.all_trips: List[Dict] = crud.get_trips(db=next(get_db()))
        self.all_calendars: List[Dict] = crud.get_calendars(db=next(get_db()))

    
    def nearest_departures_to_up(
        self, lat: str, lon: str, age:int, start_time:str = None, count_stop: int = 5, count_departure_on_stop: int = 2, stops: List[Dict] = None
    ) -> List[Dict]:
        _stops = self.all_stops if stops is None else stops
        _start_time =  datetime.now() if start_time is None else datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")

        # # key(stop_id): value(distance between stop_id and point(lat, lon))
        # distances = {
        #     stop.get("stop_id"): self.calc_distance(
        #         lat, lon, stop.get("stop_lat"), stop.get("stop_lon")
        #     )
        #     for stop in _stops
        # }

        # ordered_stops = sorted(
        #     _stops, key=lambda stop: distances.get(stop.get("stop_id"))
        # )

        # _radio = self.get_radio_according_age(age)
        # stops_within_radio = [stop for stop in ordered_stops if distances.get(stop.get("stop_id")) < _radio]
        # return stops_within_radio[:count]
        return
