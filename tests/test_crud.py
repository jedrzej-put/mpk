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


# def test_get_stop_times_by_stop_id(get_session):
#    result = crud.get_stop_times_by_stop_id(db=get_session, stop_id="4100")
#    LOGGER.info(result[0])
#    assert len(result) == 301


def test_get_stop_times_greater_time(get_session):
    result = crud.get_stop_times_greater_departure_time(
        db=get_session, curr_time=timedelta(hours=0, minutes=1, seconds=0)
    )
    LOGGER.info(result[0])
    assert None
