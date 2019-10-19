from unittest import TestCase

import openweather


class Testopenweather(TestCase):


    def test_options_tokens(self):
        testObject = openweather.options_tokens()

        pass


    def test_temperature(self):
        testObject = openweather.api_token_input()
        testObject.api_key = "08fce8ac44b0fe40a029e7d1a0b987a2"
        testObject.city_name = "Mumbai"

        current = openweather.options_tokens()





