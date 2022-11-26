from sqlalchemy import MetaData
from ..database.models import Route, City, Trip, StopTime, Stop, Calendar
from ..database.database import SessionLocal, engine
from .ReadFile import ReadFile
from ..database.Model import Model
import re
from datetime import datetime, date, time, timedelta

class LoadData():
    def __init__(self):
        self.db_session = SessionLocal()
        self.metadata=MetaData(engine)
    
    @staticmethod
    def convert_date_time(key, value):
        if re.search('date', key):
            return datetime.strptime(value, '%Y%m%d').date()
        elif re.search('time', key):
            return timedelta(*[int(_) for _ in value.split(':')])
        elif re.search('date_time', key):
            return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
        else:
            return value
        
    def load_data_from_file(self, file_name: str, model: Model) -> None:
        try:
            data = ReadFile(file_name)
            for line in data.get_data_row():
                record = model(**{key: self.convert_date_time(key, value) for key, value in zip(model.keys_names(), line)})
                self.db_session.add(record)
            self.db_session.commit()
        except Exception as e:
            print(e)
            self.db_session.rollback()
        finally:
            self.db_session.close()
    
    def __call__(self) -> None:
        self.load_data_from_file('./assets/cities.csv', City)
        self.load_data_from_file('./assets/routes-wroclaw.csv', Route)
        self.load_data_from_file('./assets/stop_times.csv', StopTime)
        self.load_data_from_file('./assets/stops.csv', Stop)
        self.load_data_from_file('./assets/trips.csv', Trip)
        self.load_data_from_file('./assets/calendar.csv', Calendar)

            