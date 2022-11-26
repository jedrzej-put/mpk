from src.package.classes.StopsController import StopsController
from src.package.database.models import Route, City
import pytest, logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

@pytest.fixture
def stops_controller():
    return StopsController()

def test_all_stops(stops_controller):
    LOGGER.info(stops_controller.all_stops[0])
    assert stops_controller.all_stops[0] == {'stop_id': '15', 'stop_code': '12525', 'stop_name': 'Metalowców', 'stop_lat': '51.13382609', 'stop_lon': '16.95673512'}


def test_calc_distance():
    lat1 = "52.2296756"
    lon1 = "21.0122287"
    lat2 = "52.406374"
    lon2 = "16.9251681"
    distance = StopsController.calc_distance(lat1, lon1, lat2, lon2)
    assert pytest.approx(278546, rel=10, abs=10) == distance