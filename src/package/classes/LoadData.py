from sqlalchemy import MetaData
from ..database.models import  Route, City, Model
from ..database.database import SessionLocal, engine
from .ReadFile import ReadFile


class LoadData():
    def __init__(self):
        self.db_session = SessionLocal()
        self.metadata=MetaData(engine)
    
    def load_data_from_file(self, file_name: str, model: Model) -> None:
        try:
            data = ReadFile(file_name)
            for line in data.get_data_row():
                record = model(**{key: value for key, value in zip(model.keys_names(), line)})
                self.db_session.add(record)
            self.db_session.commit()
        except:
            self.db_session.rollback()
        finally:
            self.db_session.close()
    
    def __call__(self) -> None:
        self.load_data_from_file('./assets/cities.csv', City)
        self.load_data_from_file('./assets/routes-wroclaw.csv', Route)

            