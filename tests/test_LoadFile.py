from src.package.classes.LoadData import LoadData
from src.package.database.models import Route, City
from src.package.database import crud
import pytest, logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

@pytest.fixture
def load_data():
    return LoadData()


def test_load_data_from_city(load_data):
    load_data.load_data_from_file('./assets/cities.csv', City)
    
    result = crud.get_cities(load_data.db_session)
    assert result == [{'city_id': '1', 'city_name': 'Wroclaw'}]

    
def test_load_data_from_route(load_data):
    load_data.load_data_from_file('./assets/routes.csv', Route)
    
    result = crud.get_routes(load_data.db_session)
    assert result[0] == {'route_id': 'A', 'route_short_name': 'A', 'route_desc': 'KOSZAROWA (SZPITAL) - Koszarowa - Berenta - Aleja Kromera - Wyszyńskiego - pl. Powstańców Warszawy - Oławska - Podwale - Świdnicka - Krucza - Inżynierska - Hallera - Grabiszyńska - Solskiego - Aleja Piastów - Racławicka - Skarbowców - Sowia - Karkonoska - KRZYKI|KRZYKI - Sowia - Skarbowców - Racławicka - Aleja Piastów - Solskiego - Grabiszyńska - Hallera - Aleja Pracy - Inżynierska - Krucza - Wielka - Świdnicka - Kościuszki - Krasińskiego - pl. Powstańców Warszawy - Wyszyńskiego - Boya-Żeleńskiego - Berenta - Kasprowicza - Czajkowskiego - Koszarowa - KOSZAROWA (SZPITAL)'}


