import pytest, logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

@pytest.fixture
def data():
    return []


def test_empty(data):
    LOGGER.info(data)
    assert len(data) == 0