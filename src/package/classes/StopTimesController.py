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
from toolz.functoolz import compose_left
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
        target_lat: str,
        target_lon: str,
        current_time: str = None,
        count_stop: int = 5,
        count_departure_on_stop: int = 2,
        stops: List[Dict] = None,
    ):
        self.lat = lat
        self.lon = lon
        self.target_lat = target_lat
        self.target_lon = target_lon
        self.age = age
        # self.all_trips: List[Dict] = crud.get_trips(db=next(get_db()))
        # self.all_calendars: List[Dict] = crud.get_calendars(db=next(get_db()))
        self.all_stops: List[Dict] = crud.get_stops(db=next(get_db()))
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
        LOGGER.info(f"CURRENT TIME: {self.start_datetime}")

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
        departures_after_start_timedelta_before_midnight = [
            _
            for _ in all_departures
            if self.time_to_timedelta(_.get("departure_time"))
            >= self.start_time_deltatime
        ]

        # """sort departures by time left until departure"""
        time_left_until_departure = {
            _.get("auto_increment_id"): (
                self.time_to_timedelta(_.get("departure_time"))
                - self.start_time_deltatime
            )
            for _ in all_departures
        }
        departures_after_start_timedelta_before_midnight.sort(
            key=lambda x: time_left_until_departure.get(x.get("auto_increment_id"))
        )
        complementary_departures = []
        if (
            len(departures_after_start_timedelta_before_midnight)
            < self.count_departure_on_stop
        ):
            complementary_departures = sorted(
                all_departures,
                key=lambda x: time_left_until_departure.get(x.get("auto_increment_id")),
                reverse=True,
            )

        departures_after_start_timedelta_before_midnight.extend(
            complementary_departures
        )
        for x in departures_after_start_timedelta_before_midnight:
            x["time_left"] = time_left_until_departure.get(x.get("auto_increment_id"))
        return departures_after_start_timedelta_before_midnight

    def correct_weekday_based_one_time(
        self, current_weekday, departure_time: str
    ) -> int:
        """correct weekday based one time"""
        if self.start_time_deltatime < self.time_to_timedelta(departure_time):
            return current_weekday
        else:
            return current_weekday + 1

    def verify_service(
        self, current_weekday: int, stop_time: Dict, calendar: Dict
    ) -> bool:
        if (
            self.start_datetime.date()
            < datetime.strptime(calendar.get("start_date"), "%Y-%m-%d").date()
        ):
            return False
        elif (
            self.start_datetime.date()
            > datetime.strptime(calendar.get("end_date"), "%Y-%m-%d").date()
        ):
            return False
        else:
            num_day_to_day_name = {
                0: "monday",
                1: "yuesday",
                2: "wednesday",
                3: "thursday",
                4: "friday",
                5: "saturday",
                6: "sunday",
            }
            current_day_name = num_day_to_day_name.get(current_weekday)
            if calendar.get(current_day_name) == "1":
                return True
            else:
                return False

    def verify_calendar_current_time(self, stop_time: Dict) -> Dict | None:
        current_weekday = self.correct_weekday_based_one_time(
            self.start_datetime.weekday(), stop_time.get("departure_time")
        )
        calendar = crud.get_calendar_by_stop_time(
            db=next(get_db()), stop_time=stop_time
        )
        LOGGER.info(calendar)
        result = (
            stop_time
            if self.verify_service(current_weekday, stop_time, calendar)
            else None
        )
        return result

    def get_distance_target_location_stop_time(self, stop_time) -> float:
        stop_id = stop_time.get("stop_id")
        stop = crud.get_stop_by_stop_id(db=next(get_db()), stop_id=stop_id)
        distance = StopsController.calc_distance(
            lat1=stop.get("stop_lat"),
            lon1=stop.get("stop_lon"),
            lat2=self.target_lat,
            lon2=self.target_lon,
        )
        return distance

    def get_next_stop_time(self, stop_time) -> float:
        trip_id = stop_time.get("trip_id")
        stop_sequence = stop_time.get("stop_sequence")
        stop_times_in_trip = crud.get_stop_times_by_trip_id(
            db=next(get_db()), trip_id=trip_id
        )
        greater_stop_sequence = (
            lambda ref_stop_sequence, stop_time: True
            if int(ref_stop_sequence) < int(stop_time.get("stop_sequence"))
            else False
        )
        stop_times_greater_stop_sequence = [
            _ for _ in stop_times_in_trip if greater_stop_sequence(stop_sequence, _)
        ]
        next_stop_time = min(
            stop_times_greater_stop_sequence,
            key=lambda stop_time: int(stop_time.get("stop_sequence")),
        )

        return next_stop_time

    def verify_direction(self, stop_time: Dict) -> Dict | None:
        current_distance = self.get_distance_target_location_stop_time(
            stop_time=stop_time
        )
        next_stop_time = self.get_next_stop_time(stop_time=stop_time)
        next_stop_time_distance = self.get_distance_target_location_stop_time(
            stop_time=next_stop_time
        )
        LOGGER.info(f"current_distance: {current_distance}\t next_distance: {next_stop_time_distance}")
        return stop_time if next_stop_time_distance < current_distance else None

    def verify_stop_time_with_compose(self, stop_time) -> Dict | None:
        return compose_left(self.verify_calendar_current_time, self.verify_direction)(stop_time)
    
    def valid_stop_time_generator_to_up(self, stop_id) -> Dict:
        stop_times = self.get_ordered_departures_of_stop(stop_id=stop_id)
        count=0
        for stop_time in stop_times:
            result = self.verify_stop_time_with_compose(stop_time)
            if result != None:
                count += 1
                yield result
            if count >= self.count_departure_on_stop:
                break

    def get_departures_from_stop(self, stop):
        stop_id = stop.get("stop_id")
        return [_ for _ in self.valid_stop_time_generator_to_up(stop_id)]
    
    def get_departures_from_stop_to_process(self):
        return {stop: self.get_departures_from_stop(stop) for stop in self.stops_to_process}