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

class Testopenweather(unittest.TestCase):

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
        testObject.pressure = True
        # print(testObject.pressure)
        # print("asjdkashkjdhaskj")
        # print(openweather.options_tokens().pressure)
        self.assertEqual(False, openweather.options_tokens().pressure, "FailedFailed")

    def test_city(self):
        # city_name=true , city_id=false, city_coord=false, city_zip =false ASSERTTRUE
        testObject = openweather.options_tokens()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        testObject.city_name = "London"
        testObject.sunrise = True
        # testObject.city_id = 400

        self.assertEqual(False, openweather.multiple_locations(testObject), "Failed")

    def test_id(self):
        # city_name=false , city_id=true, city_coord=false, city_zip =false
        testObject = openweather.options_tokens()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        #testObject.city_name = "London"
        testObject.sunrise = True
        testObject.city_id = 400

        self.assertEqual(False, openweather.multiple_locations(testObject), "Failed")


    def test_coord(self):
        # city_name=false , city_id=false, city_coord=true, city_zip =false
        testObject = openweather.options_tokens()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        #testObject.city_name = "London"
        testObject.sunrise = True
        testObject.geographical_coordinates = {"lon":-0.13,"lat":51.51}

        self.assertEqual(False, openweather.multiple_locations(testObject), "Failed")

    def test_zip(self):
        #city_name=false , city_id=false, city_coord=false, city_zip =true
        testObject = openweather.options_tokens()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        #testObject.city_name = "London"
        testObject.sunrise = True
        testObject.zip_code = 200

        self.assertEqual(False, openweather.multiple_locations(testObject), "Failed")

    def test_location1(self):
        #city_name=true , city_id=true, city_coord=false, city_zip =false // consider id ASSERT FALSE
        testObject = openweather.options_tokens()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        testObject.city_name = "London"
        testObject.sunrise = True
        testObject.city_id = 400

        self.assertEqual(True, openweather.multiple_locations(testObject), "Failed")

    def test_location3(self):
        #city_name=true , city_id=true, city_coord=true, city_zip =false // consider coord ASSERT FALSE
        testObject = openweather.options_tokens()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        testObject.city_name = "London"
        testObject.sunrise = True
        testObject.city_id = 400
        testObject.geographical_coordinates = {"lon":144.96,"lat":-37.81}

        self.assertEqual(True, openweather.multiple_locations(testObject), "Failed")

    def test_location4(self):
        #city_name=true , city_id=true, city_coord=false, city_zip =true // consider zip ASSERT FALSE
        testObject = openweather.options_tokens()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        testObject.city_name = "London"
        testObject.sunrise = True
        testObject.zip_code = 200
        testObject.city_id = 400

        self.assertEqual(True, openweather.multiple_locations(testObject), "Failed")


'''
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
    
    # def test_location2(self):
    #     # city_name=false , city_id=false, city_coord=false, city_zip =false //consider name ASSERT FALSE
    #     testObject = openweather.options_tokens()
    #     testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
    #     # testObject.city_name = "London"
    #     testObject.sunrise = True
    #     #testObject.zip_code = 200
    #
    #     self.assertEqual(True, openweather.multiple_locations(testObject), "Failed")

'''






if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-api=08fce8ac44b0fe40a029e7d1a0b987a2', default='My Input')
    parser.add_argument('-city=', default='London')
    parser.add_argument('-time')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args(['-time'])
    #Go do something with args.input and args.filename

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[0:] = args.unittest_args
    unittest.main()


