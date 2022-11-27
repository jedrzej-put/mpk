from src.package.classes.StopTimesController import StopTimesController
from src.package.database.models import Route, City
import pytest, logging, datetime

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()


@pytest.fixture
def stop_times_controller():
    return StopTimesController(
        "51.13382609", "16.95673511", 20, current_time="2021-11-04T22:24:00"
    )


@pytest.fixture
def stop_time_zajezdnia_obornicka_ser3():
    return {
        "auto_increment_id": "735431",
        "trip_id": "3_11553791",
        "arrival_time": "22:24:00",
        "departure_time": "22:24:00",
        "stop_id": "4562",
        "stop_sequence": "32",
        "time_left": datetime.timedelta(0),
    }


@pytest.fixture
def stop_time_zajezdnia_obornicka_ser4():
    return {
        "auto_increment_id": "737672",
        "trip_id": "4_11556732",
        "arrival_time": "22:24:00",
        "departure_time": "22:24:00",
        "stop_id": "4562",
        "stop_sequence": "32",
        "time_left": datetime.timedelta(0),
    }


@pytest.fixture
def stop_time_zajezdnia_obornicka_ser6():
    return {
        "auto_increment_id": "585371",
        "trip_id": "6_11541583",
        "arrival_time": "22:29:00",
        "departure_time": "22:29:00",
        "stop_id": "4562",
        "stop_sequence": "16",
        "time_left": datetime.timedelta(seconds=300),
    }


@pytest.fixture
def stop_time_litewska_ser3():
    return {
        "auto_increment_id": "46818",
        "trip_id": "3_11554675",
        "arrival_time": "22:25:00",
        "departure_time": "22:25:00",
        "stop_id": "4562",
        "stop_sequence": "0",
        "time_left": datetime.timedelta(seconds=60),
    }


# def test_time_to_timedelta(stop_times_controller):
#     LOGGER.info(stop_times_controller.start_time_deltatime)
#     testcase = StopTimesController.time_to_timedelta("23:24:22")
#     LOGGER.info(testcase)

#     assert testcase == datetime.timedelta(hours=23, minutes=24, seconds=22)
#     assert testcase > stop_times_controller.start_time_deltatime ## czas odpalania testu
#     assert testcase < datetime.timedelta(hours=23, minutes=51, seconds=1)


def test_get_ordered_departures_of_stop(stop_times_controller):
    result = stop_times_controller.get_ordered_departures_of_stop(stop_id="4562")
    LOGGER.info(result[0])
    assert result[0].get("stop_id") == "4562"
