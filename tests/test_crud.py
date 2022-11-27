from src.package.database.models import StopTime
from src.package.database.Model import Model
from src.package.database import crud
from src.dependencies import get_db
import pytest, logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()


@pytest.fixture
def get_session():
    return next(get_db())


def test_get_stop_times_by_stop_id(get_session):
    result = crud.get_stop_times_by_stop_id(db=get_session, stop_id="4100")
    LOGGER.info(result[0])
    assert len(result) == 301


def test_get_trip_by_trip_id(get_session):
    result = crud.get_trip_by_trip_id(db=get_session, trip_id="3_11553791")
    LOGGER.info(result)
    assert result == {
        "route_id": "134",
        "service_id": "3",
        "trip_id": "3_11553791",
        "trip_headsign": "Zajezdnia Obornicka",
    }


def test_get_calendar_by_service_id(get_session):
    result = crud.get_calendar_by_service_id(db=get_session, service_id="3")
    LOGGER.info(result)
    assert result == {
        "service_id": "3",
        "monday": "0",
        "tuesday": "0",
        "wednesday": "0",
        "thursday": "0",
        "friday": "0",
        "saturday": "1",
        "sunday": "0",
        "start_date": "2022-11-27",
        "end_date": "2022-12-11",
    }


def test_get_stop_by_auto_increment_id(get_session):
    result = crud.get_stop_by_auto_increment_id(
        db=get_session, auto_increment_id="735431"
    )
    LOGGER.info(result)
    assert result == {
        "auto_increment_id": "735431",
        "trip_id": "3_11553791",
        "arrival_time": "22:24:00",
        "departure_time": "22:24:00",
        "stop_id": "4562",
        "stop_sequence": "32",
    }


def test_get_calendar_by_stop_time(get_session):
    stop_time = {
        "auto_increment_id": "46818",
        "trip_id": "3_11554675",
        "arrival_time": "22:25:00",
        "departure_time": "22:25:00",
        "stop_id": "4562",
        "stop_sequence": "0",
    }
    result = crud.get_calendar_by_stop_time(get_session, stop_time)
    assert result == {
        "service_id": "3",
        "monday": "0",
        "tuesday": "0",
        "wednesday": "0",
        "thursday": "0",
        "friday": "0",
        "saturday": "1",
        "sunday": "0",
        "start_date": "2022-11-27",
        "end_date": "2022-12-11",
    }
