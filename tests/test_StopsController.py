from src.package.classes.StopsController import StopsController
from src.package.database.models import Route, City
import pytest, logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

@pytest.fixture
def stops_controller():
    return StopsController()

# def test_all_stops(stops_controller):
#     LOGGER.info(stops_controller.all_stops[0])
#     assert stops_controller.all_stops[0] == {'stop_id': '15', 'stop_code': '12525', 'stop_name': 'Metalowców', 'stop_lat': '51.13382609', 'stop_lon': '16.95673512'}

# def test_all_stops(stops_controller):
#     LOGGER.info(stops_controller.all_stops[0])
#     assert stops_controller.all_stops[0].get('stop_id') == "15"


# def test_calc_distance():
#     lat1 = "52.2296756"
#     lon1 = "21.0122287"
#     lat2 = "52.406374"
#     lon2 = "16.9251681"
#     distance = StopsController.calc_distance(lat1, lon1, lat2, lon2)
#     assert pytest.approx(278546, rel=10, abs=10) == distance


# def test_nearest_stops_to_up_count(stops_controller):
#     stops = stops_controller.all_stops[:3]
#     lat = "51.13382609"
#     lon = "16.95673511"
#     nearest_stops = stops_controller.nearest_stops_to_up(lat=lat, lon=lon, count=2, stops=stops)
#     LOGGER.info(nearest_stops)
#     assert nearest_stops[0]["stop_id"] == "15" #metalcow
#     assert nearest_stops[1]["stop_id"] == "40" #park

# def test_get_radio_according_age():
#     assert StopsController.get_radio_according_age(15) == 1000
#     assert StopsController.get_radio_according_age(16) == 5000
#     assert StopsController.get_radio_according_age(25) == 5000
#     assert StopsController.get_radio_according_age(35) == 2000
#     assert StopsController.get_radio_according_age(40) == 1000
#     assert StopsController.get_radio_according_age(65) == 500
#     assert StopsController.get_radio_according_age(75) == 100


def test_test_compose(stops_controller):
    LOGGER.info(stops_controller.test_compose(4))
    assert stops_controller.test_compose(4) == 10