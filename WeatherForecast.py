import requests
import argparse
from datetime import datetime

# For action:
"""
The action has two different options, store and store_true

store: Requires an  argument to be inserted through the command lined
store_true: This doesnt require an argument
 
"""

# For destination:
"""
This is the name of the token
"""

def options_tokens():

    parser = argparse.ArgumentParser()

    parser.add_argument('--api', action='store', dest='api_key',
                        help='An API token is required to perform the API request')

    parser.add_argument('--city', action='store', dest='city_name',
                        help='Perform query based on the name of the City')

    parser.add_argument('--cid', action='store', dest='city_id',
                        help='Perform query based on the name of the City ID')

    parser.add_argument('--gc', action='store', dest='geographic_coordinates',
                        help='Perform query based on the geographic coordinates given in latitude,longitude')

    parser.add_argument('--z', action='store', dest='zip_code',
                        help='Perform query based on the zip-code, country code')

    parser.add_argument('--temp', action='store', nargs='?', const='celsius', dest='temperature',
                        help='This will give us the temperature in celsius')

    parser.add_argument('--time', action='store_true', dest='time',
                        help='This will display the current time at the given location')

    parser.add_argument('--pressure', action='store_true', dest='pressure',
                        help='This will display the current pressure(in Pa) at the given location')

    parser.add_argument('--cloud', action='store_true', dest='cloud',
                        help='This will display the current cloud conditions at the given location')

    parser.add_argument('--humidity', action='store_true', dest='humidity',
                        help='This will display the current humidity at the given location')

    parser.add_argument('--wind', action='store_true', dest='wind',
                        help='This will display the current wind speed at the given location')

    parser.add_argument('--sunset', action='store_true', dest='sunset',
                        help='This will display the current sunset time at the given location')

    parser.add_argument('--sunrise', action='store_true', dest='sunrise',
                        help='This will display the current sunrise time at the given location')

    options = parser.parse_args()

    return options



def print_information(response):
    """
    This function is used to print out the results to the console
    :param response:
    :return:
    """
    # This variable holds all the information in JSON format that is
    api_data = response.json()

    if options_tokens().temperature:
        print("The temperature")

    if options_tokens().time:
        time_variable = int(api_data['dt'])
        current_time = datetime.utcfromtimestamp(time_variable).strftime('%Y-%m-%d %H:%M:%S')
        print("The Current time is: ", current_time)

    if options_tokens().pressure:
        print("Pressure:", api_data['main']['pressure'])

    if options_tokens().cloud:
        print("Cloudiness:", api_data['clouds']['all'], "%")

    if options_tokens().humidity:
        print("Humidity:", api_data['main']['humidity'], "%")

    if options_tokens().wind:
        print("Wind speed:", api_data['wind']['speed'], "meter/sec")
        print("Wind degrees:", api_data['wind']['deg'])

    if options_tokens().sunset:
        sunset_variable = int(api_data['sys']['sunset'])
        sunset_time = datetime.utcfromtimestamp(sunset_variable).strftime('%Y-%m-%d %H:%M:%S')
        print("Sunset time:", sunset_time)

    if options_tokens().sunrise:
        sunrise_variable = int(api_data['sys']['sunrise'])
        time_sunrise = datetime.utcfromtimestamp(sunrise_variable).strftime('%Y-%m-%d %H:%M:%S')
        print("Sunrise time:", time_sunrise)


def multiple_locations():
    """
    This function is used to return True or False based on whether or not the user chooses multiple locations
    :return:
    True: If only one location type is chosen.
    False: If more than one type was chosen.
    """

    if options_tokens().city_name and (options_tokens().city_id or options_tokens().geographic_coordinates or options_tokens().zip_code):
        return True

    elif options_tokens().city_id and (options_tokens().city_name or options_tokens().geographic_coordinates or options_tokens().zip_code):
        return True

    elif options_tokens().geographic_coordinates and (options_tokens().city_name or options_tokens().city_id or options_tokens().zip_code):
        return True

    elif options_tokens().zip_code and (options_tokens().city_name or options_tokens().city_id or options_tokens().geographic_coordinates):
        return True

    else:
        return False


def other():

    blah = options_tokens().time or options_tokens().pressure or options_tokens().cloud\
           or options_tokens().humidity or options_tokens().wind or options_tokens().sunset\
           or options_tokens().sunrise or options_tokens().temperature

    if multiple_locations():
        print("Multiple Locations")
    else:
        if options_tokens().api_key and options_tokens().city_name and blah:
            url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
            response = requests.get(url.format(options_tokens().city_name, options_tokens().api_key))
            print_information(response)

        elif options_tokens().api_key and options_tokens().city_id and blah:
            url = "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}"
            response = requests.get(url.format(options_tokens().city_id, options_tokens().api_key))
            print_information(response)

        elif options_tokens().api_key and options_tokens().geographic_coordinates and blah:
            lat_lon = options_tokens().geographic_coordinates.split(",")
            latitude = lat_lon[0]
            longitude = lat_lon[1]
            url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"
            response = requests.get(url.format(latitude, longitude, options_tokens().api_key))
            print_information(response)

        elif options_tokens().api_key and options_tokens().zip_code and blah:
            url = "https://api.openweathermap.org/data/2.5/weather?zip={}&appid={}"
            response = requests.get(url.format(options_tokens().zip_code, options_tokens().api_key))
            print_information(response)

        elif not blah:
            print("Nothing chosen")


if __name__ == "__main__":
    other()




