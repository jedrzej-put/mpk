from src.package.database.models  import StopTime
from src.package.database.Model import Model
from src.package.classes.LoadData import LoadData

import re, datetime
import pytest, logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

@pytest.fixture
def load_data():
    return LoadData()

def test_StopTime():
   LOGGER.info(list(StopTime.keys_names()))
    

def test_MetaData():
    LOGGER.info(Model.metadata.tables)

def test_regex():
    LOGGER.info(LoadData.convert_date_time("start_date", "20221127"))
    assert LoadData.convert_date_time("start_date", "20221127") == datetime.date(2022, 11, 27)
    assert LoadData.convert_date_time("arrival_time", "26:52:00") == datetime.timedelta(26, 52, 0)