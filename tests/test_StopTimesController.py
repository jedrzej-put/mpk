from src.package.classes.StopTimesController import StopTimesController
from src.package.database.models import Route, City
import pytest, logging, datetime

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()


@pytest.fixture
def stop_times_controller():
    return StopTimesController("51.13382609", "16.95673511", 20, current_time="2021-11-04T22:24:00")


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
