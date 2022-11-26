from typing import Dict, List
from sqlalchemy.ext.declarative import declarative_base

class NormalModel():
    def toDict(self) -> Dict:
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    
    @classmethod
    def keys_names(cls) -> List:
        # return [str(c.name) for c in cls.__table__.columns if c.name != 'auto_increment_id']
        return [str(c.name) for c in cls.__table__.columns]

           
Model = declarative_base(cls=NormalModel)