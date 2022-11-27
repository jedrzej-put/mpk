from ..database import crud
from ..database.models import Route, City
from ..database.Model import Model
from ...dependencies import get_db
from sqlalchemy.orm import Session
from decimal import *
from math import sin, cos, sqrt, atan2, radians
from typing import List, Dict, TypedDict
from toolz.functoolz import compose
from datetime import datetime, timedelta, time, date
from .StopsController import StopsController
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()


class StopTimesController:
    def __init__(
        self,
        lat: str,
        lon: str,
        age: int,
        current_time: str = None,
        count_stop: int = 5,
        count_departure_on_stop: int = 2,
        stops: List[Dict] = None,
    ):
        self.all_trips: List[Dict] = crud.get_trips(db=next(get_db()))
        self.all_calendars: List[Dict] = crud.get_calendars(db=next(get_db()))
        self.start_datetime = (
            datetime.now()
            if current_time is None
            else datetime.fromisoformat(current_time)
        )
        self.start_time_deltatime = timedelta(
            hours=self.start_datetime.hour,
            minutes=self.start_datetime.minute,
            seconds=self.start_datetime.second,
        )
        _stops = self.all_stops if stops is None else stops
        self.stops_to_process = StopsController().nearest_stops_to_up(
            lat, lon, age, count=count_stop, stops=_stops
        )
        self.count_departure_on_stop = count_departure_on_stop
        LOGGER.info(f"CURRENT TIME: {self.start_time_deltatime}")

    def nearest_departures_run(self) -> List[Dict]:
        pass

    ## methods for processing single stop
    @staticmethod
    def time_to_timedelta(_time: str) -> timedelta:
        hours, minutes, seconds = [int(_) for _ in _time.split(":")]
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)

    def get_ordered_departures_of_stop(self, stop_id: str) -> List[Dict]:
        all_departures: List[Dict] = crud.get_stop_times_by_stop_id(
            db=next(get_db()), stop_id=stop_id
        )

        # """filter to departure_time will be greater than current time"""
        departures_after_start_timedelta = [
            _
            for _ in all_departures
            if self.time_to_timedelta(_.get("departure_time"))
            > self.start_time_deltatime
        ]
        _flag = False
        if len(departures_after_start_timedelta) == 0:
            pass

        # """sort departures by time left until departure"""
        time_left_until_departure = {
            _.get("auto_increment_id"): (
                self.time_to_timedelta(_.get("departure_time"))
                - self.start_time_deltatime
            )
            for _ in departures_after_start_timedelta
        }
        departures_after_start_timedelta.sort(
            key=lambda x: time_left_until_departure.get(x.get("auto_increment_id"))
        )
        return departures_after_start_timedelta
