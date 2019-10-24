from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch
import openweather
import unittest
import pytest
import requests
import argparse
import sys

# dummydata = {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"base":"stations","main":{"temp":285.13,"pressure":1007,"humidity":93,"temp_min":284.15,"temp_max":286.15},"visibility":5000,"wind":{"speed":1.5,"deg":70},"rain":{},"clouds":{"all":40},"dt":1571864297,"sys":{"type":1,"id":1414,"country":"GB","sunrise":1571812642,"sunset":1571849528},"timezone":3600,"id":2643743,"name":"London","cod":200}
# response = Mock()
# response.json.return_value = dummydata
# @patch('openweather.requests')
## Regardless of what the command line inputs are, if they pass all the conditions, the above dummydata is used to display the results.

class Testopenweather(TestCase):

    # def test_options_tokens(self):
    #     testObject = openweather.options_tokens()
    #
    #     pass
    #
    # def test_noAPI(self):
    #
    # def test_noCity(self):
    #
    # def test_noAPIorCity(self):

    def test_wind(self):
        ##ask for api, city and wind, then assert wind?
        testObject = openweather.options_tokens()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        testObject.city_name = "London"
        testObject.wind = "0.3"

        #options = (api_key=None, city_id=None, city_name=None, cloud=False, geographic_coordinates=None, humidity=False, pressure=False, sunrise=False, sunset=False, temperature=None, time=False, wind=False, zip_code=None)
        # blah = openweather.multiple_locations()
        # print(blah)
        testObjectTest = openweather.options_tokens()
        print(testObjectTest)
        print(testObject)
        passit = openweather.api_token_input()
        print("Passit")
        print(passit)


        url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=08fce8ac44b0fe40a029e7d1a0b987a2"
        response = requests.get(url)
        data = response.json()
        #self.assertEqual(testObjectTest['sunrise'], data['sys']['sunrise'], "Failed")




"""
    def test_temperature(self):
        testObject = openweather.api_token_input()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        testObject.city_name = "Mumbai"

        current = openweather.options_tokens()

    


    def test_humidity(self):

        self.assertTrue(self.options_tokens().humidity)

    def test_cloud(self):

        self.assertTrue(self.options_tokens().cloud)

    def test_time(self):

        self.assertTrue(self.options_tokens().time)

    def test_sunset(self):

        self.assertTrue(self.options_tokens().sunset)

    def test_sunrise(self):

        self.assertTrue(self.options_tokens().sunrise)

    def test_help(self):

        self.assertTrue(self.options_tokens().help)

    def test_pressure(self):

        # self.assertTrue(self.options_tokens().pressure)

     def test_allCompatibleOptions(self):
         pass
    #if they all test true individually, they should all test true when called together


    ##location


    def test_city(self):
        #city_name=true , city_id=false, city_coord=false, city_zip =false ASSERTTRUE
        self.assertTrue(self.options_tokens().city_name)

    def test_id(self):
        # city_name=false , city_id=true, city_coord=false, city_zip =false
        self.assertTrue(self.options_tokens().city_id)

    def test_coord(self):
        # city_name=false , city_id=false, city_coord=true, city_zip =false
        self.assertTrue(self.options_tokens().geographic_coordinates)

    def test_zip(self):
        #city_name=false , city_id=false, city_coord=false, city_zip =true
        self.assertTrue(self.options_tokens().zip_code)

    def test_location1(self):
        #city_name=true , city_id=true, city_coord=false, city_zip =false // consider id ASSERT FALSE
        self.assertFlase(self.multiple_locations())

    def test_location2(self):
        # city_name=false , city_id=false, city_coord=false, city_zip =false //consider name ASSERT FALSE
        self.assertFlase(self.multiple_locations())

    def test_location3(self):
        #city_name=true , city_id=true, city_coord=true, city_zip =false // consider coord ASSERT FALSE
        self.assertFlase(self.multiple_locations())

    def test_location4(self):
        #city_name=true , city_id=true, city_coord=false, city_zip =true // consider zip ASSERT FALSE
        self.assertFalse(self.multiple_locations())

"""
if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-api=08fce8ac44b0fe40a029e7d1a0b987a2', default='My Input')
    parser.add_argument('-city=', default='London')
    parser.add_argument('-time')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args(['-time'])
    #Go do something with args.input and args.filename

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args
    unittest.main()


