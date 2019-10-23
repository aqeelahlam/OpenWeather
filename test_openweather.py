from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch
import openweather



dummydata = "{"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"base":"stations","main":{"temp":285.13,"pressure":1007,"humidity":93,"temp_min":284.15,"temp_max":286.15},"visibility":5000,"wind":{"speed":1.5,"deg":70},"rain":{},"clouds":{"all":40},"dt":1571864297,"sys":{"type":1,"id":1414,"country":"GB","sunrise":1571812642,"sunset":1571849528},"timezone":3600,"id":2643743,"name":"London","cod":200}"
response = Mock()
response.json.return_value = dummydata
@patch('openweather.requests')
## Regardless of what the command line inputs are, if they pass all the conditions, the above dummydata is used to display the results.

class Testopenweather(TestCase):


    def test_options_tokens(self):
        testObject = openweather.options_tokens()

        pass

    def test_noAPI(self):

    def test_noCity(self):

    def test_noAPIorCity(self):



    def test_temperature(self):
        testObject = openweather.api_token_input()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        testObject.city_name = "Mumbai"

        current = openweather.options_tokens()

    def test_wind(self):
        ##ask for api, city and wind, then assert wind?
        self.assertTrue(self.options_tokens().wind)


    def test_humidity(self):


    def test_cloud(self):


    def test_time(self):


    def test_sunset(self):


    def test_sunrise(self):


    def test_help(self):


    def test_pressure(self):


    def test_location(self):


    def test_allCompatibleOptions(self):

    ##location


    def test_city(self):
        #city_name=true , city_id=false, city_coord=false, city_zip =false ASSERTTRUE

    def test_id(self):
        # city_name=false , city_id=true, city_coord=false, city_zip =false

    def test_coord(self):
        # city_name=false , city_id=false, city_coord=true, city_zip =false

    def test_zip(self):
        #city_name=false , city_id=false, city_coord=false, city_zip =true

    def test_location2(self):
        #city_name=true , city_id=true, city_coord=false, city_zip =false // consider id ASSERT FALSE

    def test_location2(self):
        # city_name=false , city_id=false, city_coord=false, city_zip =false //consider name ASSERT FALSE

    def test_location2(self):
        #city_name=true , city_id=true, city_coord=true, city_zip =false // consider coord ASSERT FALSE

    def test_location2(self):
        #city_name=true , city_id=true, city_coord=false, city_zip =true // consider zip ASSERT FALSE





