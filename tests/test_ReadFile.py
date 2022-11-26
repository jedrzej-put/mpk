from src.package.classes.ReadFile import ReadFile
import pytest, logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

@pytest.fixture
def file_name():
    return './assets/cities.csv'

def test_read_cities(file_name):
    read_file = ReadFile(file_name)

    assert ['1', 'Wroclaw'] == next(read_file.get_data_row())
    