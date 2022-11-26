from pydantic import BaseModel
from datetime import date, time
from enum import IntEnum
class City(BaseModel):
    city_id: int
    city_name: str 

class Route(BaseModel):
    route_id: str
    route_short_name: str 
    route_desc: str

class Trip(BaseModel):
    route_id: str
    service_id: str
    trip_id: str
    trip_headsign: str

class Stop(BaseModel):
    stop_id: str
    stop_code: str
    stop_name: str
    stop_lat: float
    stop_lon: float

class StopTime(BaseModel):
    auto_increment_id: int
    trip_id: str
    arrival_time: time
    departure_time: time
    stop_id: str
    stop_code: str
    stop_sequence: int
    
    
class Calendar(BaseModel):
    service_id: str
    monday: IntEnum
    tuesday: IntEnum
    wednesday: IntEnum
    thursday: IntEnum
    friday: IntEnum
    saturday: IntEnum
    sunday: IntEnum
    start_date: date
    end_date: date