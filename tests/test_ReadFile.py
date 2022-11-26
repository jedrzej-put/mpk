from src.package.database.models  import StopTime
from src.package.database.Model import Model

import pytest, logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_StopTime():
    pass
#    LOGGER.info(list(StopTime.keys_names()))
    

def test_MetaData():
    LOGGER.info(Model.metadata.tables)