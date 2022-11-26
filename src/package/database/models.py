from sqlalchemy import Column, Integer, String
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



