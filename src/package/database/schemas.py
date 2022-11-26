from pydantic import BaseModel


class City(BaseModel):
    city_id: int
    city_name: str 

class Route(BaseModel):
    route_id: str
    route_short_name: str 
    route_desc: str