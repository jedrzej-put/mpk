from src.package.classes.StopTimesController import StopTimesController
from src.package.database.models import Route, City
import pytest, logging, datetime
from src.dependencies import get_db
from src.package.database import crud

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()


@pytest.fixture
def stop_metalowcow():
    return {
        "stop_id": "15",
        "stop_code": "12525",
        "stop_name": "Metalowców",
        "stop_lat": "51.13382609",
        "stop_lon": "16.90",
    }


@pytest.fixture
def stop_times_controller_thursday():
    return StopTimesController(
        "51.13382609",
        "16.96673511",
        20,
        "51.14062655",
        "16.95825689",
        current_time="2021-11-04T22:24:00",
    )


@pytest.fixture
def stop_times_controller_saturday():
    return StopTimesController(
        "51.13382609",
        "16.96673511",
        20,
        "51.14062655",
        "16.95825689",
        current_time="2022-12-03T22:24:00",
    )


def get_stop_time_by_autoincrement_id(stop_time_id):
    stop_times_controller = StopTimesController(
        "51.13382609",
        "16.95673511",
        20,
        "51.14062655",
        "16.95825689",
        current_time="2021-11-04T22:24:00",
    )
    stop_time = crud.get_stop_by_auto_increment_id(
        db=next(get_db()), auto_increment_id=stop_time_id
    )
    stop_time["time_left"] = (
        stop_times_controller.time_to_timedelta(stop_time.get("departure_time"))
        - stop_times_controller.start_time_deltatime
    )
    return stop_time


# def test_time_to_timedelta(stop_times_controller_thursday):
#     LOGGER.info(stop_times_controller_thursday.start_time_deltatime)
#     testcase = StopTimesController.time_to_timedelta("23:24:22")
#     LOGGER.info(testcase)

#     assert testcase == datetime.timedelta(hours=23, minutes=24, seconds=22)
#     assert testcase > stop_times_controller_thursday.start_time_deltatime ## czas odpalania testu
#     assert testcase < datetime.timedelta(hours=23, minutes=51, seconds=1)


# def test_get_ordered_departures_of_stop(stop_times_controller_thursday):
#     result = stop_times_controller_thursday.get_ordered_departures_of_stop(stop_id="4562")
#     LOGGER.info(result[0])
#     assert result[0].get("stop_id") == "4562"

# def test_get_stop_time_by_autoincrement_id():
#     result = get_stop_time_by_autoincrement_id("46818")
#     LOGGER.info(result)
#     assert result == {
#         "auto_increment_id": "46818",
#         "trip_id": "3_11554675",
#         "arrival_time": "22:25:00",
#         "departure_time": "22:25:00",
#         "stop_id": "4562",
#         "stop_sequence": "0",
#         "time_left": datetime.timedelta(seconds=60),
#     }

# def test_verify_calendar_current_time(stop_times_controller_thursday):
#     stop_time = get_stop_time_by_autoincrement_id("46818") # only saturday serviced
#     result = stop_times_controller_thursday.verify_calendar_current_time(stop_time)
#     assert result == None


# def test_verify_calendar_current_time(stop_times_controller_saturday):
#     stop_time = get_stop_time_by_autoincrement_id("46818")  # only saturday serviced
#     result = stop_times_controller_saturday.verify_calendar_current_time(stop=None, stop_time=stop_time)
#     assert result == stop_time


def test_get_distance_target_location_stop_time(stop_times_controller_saturday):
    stop_time = get_stop_time_by_autoincrement_id("591856")  # only saturday serviced
    result = stop_times_controller_saturday.get_distance_target_location_stop_time(
        stop_time=stop_time
    )
    LOGGER.info(f"result: {result}")
    assert pytest.approx(6979, rel=10, abs=10) == result


def test_get_next_stop_time(stop_times_controller_saturday):
    stop_time = get_stop_time_by_autoincrement_id("591856")  # only saturday serviced
    next_stop_time = stop_times_controller_saturday.get_next_stop_time(stop_time)
    LOGGER.info(f"next_stop_time: {next_stop_time}")
    assert next_stop_time == {
        "auto_increment_id": "591857",
        "trip_id": "3_11455579",
        "arrival_time": "21:12:00",
        "departure_time": "21:12:00",
        "stop_id": "1809",
        "stop_sequence": "2",
    }


def test_verify_direction(stop_times_controller_saturday, stop_metalowcow):
    stop_time = get_stop_time_by_autoincrement_id("591856")  # only saturday serviced
    result = stop_times_controller_saturday.verify_direction(stop_time=stop_time)
    LOGGER.info(f"result: {result}")
    assert result == {
        "auto_increment_id": "591856",
        "trip_id": "3_11455579",
        "arrival_time": "21:11:00",
        "departure_time": "21:11:00",
        "stop_id": "15",
        "stop_sequence": "1",
        "time_left": datetime.timedelta(days=-1, seconds=82020),
    }
