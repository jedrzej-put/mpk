from sqlalchemy import Column, Integer, String, Numeric, Enum, Date, Time
from typing import Dict, List
from sqlalchemy.ext.declarative import declarative_base
from .database import Base

class NormalModel():
    def toDict(self) -> Dict:
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    
    @classmethod
    def keys_names(cls) -> List:
        return [str(c.name) for c in cls.__table__.columns]

           
Model = declarative_base(cls=NormalModel)

class City(Model):
    __tablename__ = "cities"

    city_id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String, index=True)


class Route(Model):
    __tablename__ = "routes"

    route_id = Column(String, primary_key=True, index=True)
    route_short_name = Column(String, index=True)
    route_desc = Column(String)

class Trip(Model):
    __tablename__ = "trips"

    route_id = Column(String, index=True)
    service_id = Column(String)
    trip_id = Column(String, primary_key=True, index=True) 
    trip_headsign = Column(String)

class Stop(Model):
    __tablename__ = "stops"

    stop_id = Column(String, primary_key=True, index=True)
    stop_code = Column(String)
    stop_name = Column(String)
    stop_lat = Column(Numeric)
    stop_lon = Column(Numeric)

class StopTime(Model):
    __tablename__ = "stop_times"

    trip_id = Column(String)
    arrival_time = Column(Time)
    departure_time = Column(Time)
    stop_id = Column(String)
    stop_code = Column(String)
    stop_sequence = Column(Integer)
    
    
class Calendar(Model):
    __tablename__ = "calendars"

    service_id = Column(String, primary_key=True, index=True)
    monday = Column(Enum)
    tuesday = Column(Enum)
    wednesday = Column(Enum)
    thursday = Column(Enum)
    friday = Column(Enum)
    saturday = Column(Enum)
    sunday = Column(Enum)
    start_date = Column(Date)
    end_date = Column(Date)