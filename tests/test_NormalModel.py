from src.package.classes.LoadData import LoadData
from src.package.database.models import Route, City
import pytest, logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_keys_names():
    assert ['city_id', 'city_name'] == City.keys_names()