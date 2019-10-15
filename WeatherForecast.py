import requests
import argparse
from optparse import OptionParser
from datetime import datetime

##For action:
"""
The action has two different options, store and store_true

store: Requires an  argument to be inserted through the command lined
store_true: This doesnt require an argument
 
"""

##For dest:
"""
This is the name of the token
"""



parser = OptionParser()
parser.add_option('--api', action='store', dest='api_key',
                  help='An API token is required to perform the API request')

parser.add_option('--city', action='store', dest='city_name',
                  help='Perform query based on the name of the City')

parser.add_option('--cid', action='store', dest='city_id',
                  help='Perform query based on the name of the City ID')
#
parser.add_option('--gc', action='store', dest='geographic_coordinates',
                  help='Perform query based on the geographic coordinates given in latitude,longitude')

parser.add_option('--z', action='store', dest='zip_code',
                  help='Perform query based on the zip-code, country code')

parser.add_option('--time', action='store_true', dest='time',
                  help='This will display the current time at the given location')

parser.add_option('--pressure', action='store_true', dest='pressure',
                  help='This will display the current pressure(in Pa) at the given location')

parser.add_option('--cloud', action='store_true', dest='cloud',
                  help='This will display the current cloud conditions at the given location')

parser.add_option('--humidity', action='store_true', dest='humidity',
                  help='This will display the current humidity at the given location')

parser.add_option('--wind', action='store_true', dest='wind',
                  help='This will display the current wind speed at the given location')

parser.add_option('--sunset', action='store_true', dest='sunset',
                  help='This will display the current sunset time at the given location')

parser.add_option('--sunrise', action='store_true', dest='sunrise',
                  help='This will display the current sunrise time at the given location')

(options, args) = parser.parse_args()


##START HEREEEEEEEEEE###


temperatureParser = argparse.ArgumentParser()

temperatureParser.add_argument('--temp', '-t', nargs='?', type=str, const='celcius')

c = temperatureParser.parse_args()


def print_information(response):
    """
    This function is used to print out the results to the console
    :param response:
    :return:
    """
    # This variable holds all the information in JSON format thats
    api_data = response.json()

    if options.time:
        timeVariable = int(api_data['dt'])
        currentTime = datetime.utcfromtimestamp(timeVariable).strftime('%Y-%m-%d %H:%M:%S')
        print("The Current time is: ", currentTime)

    if options.pressure:
        print("Pressure:", api_data['main']['pressure'])

    if options.cloud:
        print("Cloudiness:", api_data['clouds']['all'], "%")

    if options.humidity:
        print("Humidity:", api_data['main']['humidity'], "%")

    if options.wind:
        print("Wind speed:", api_data['wind']['speed'], "meter/sec")
        print("Wind degrees:", api_data['wind']['deg'])

    if options.sunset:
        sunsetVariable = int(api_data['sys']['sunset'])
        sunset_time = datetime.utcfromtimestamp(sunsetVariable).strftime('%Y-%m-%d %H:%M:%S')
        print("Sunset time:", sunset_time)

    if options.sunrise:
        sunriseVariable = int(api_data['sys']['sunrise'])
        time_sunrise = datetime.utcfromtimestamp(sunriseVariable).strftime('%Y-%m-%d %H:%M:%S')
        print("Sunrise time:", time_sunrise)


if options.city_name and options.city_id or options.geographic_coordinates or options.zip_code:
    print("Multiple Locations")
elif options.geographic_coordinates and options.city_name or options.city_id or options.zip_code:
    print("Multiple Locations")
elif options.city_id and options.city_name or options.geographic_coordinates or options.zip_code:
    print("Multiple Locations")
elif options.zip_code and options.city_name or options.geographic_coordinates or options.city_id:
    print("Multiple Locations")


elif options.city_name and options.api_key and options.time or options.pressure or options.cloud or options.humidity or options.wind or options.sunset or options.sunrise:
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    response = requests.get(url.format(options.city_name, options.api_key))
    print_information(response)


elif options.city_id and options.api_key and options.time or options.pressure or options.cloud or options.humidity or options.wind or options.sunset or options.sunrise:
    url = "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}"
    response = requests.get(url.format(options.city_id, options.api_key))
    print_information(response)


elif options.geographic_coordinates and options.api_key and options.time or options.pressure or options.cloud or options.humidity or options.wind or options.sunset or options.sunrise:
    lat_lon = options.geographic_coordinates.split(",")
    lat = lat_lon[0]
    lon = lat_lon[1]
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"
    response = requests.get(url.format(lat, lon, options.api_key))
    print_information(response)

elif options.zip_code and options.api_key and options.time or options.pressure or options.cloud or options.humidity or options.wind or options.sunset or options.sunrise:
    url = "https://api.openweathermap.org/data/2.5/weather?zip={}&appid={}"
    response = requests.get(url.format(options.zip_code, options.api_key))
    print_information(response)

elif not options.time or options.pressure or options.cloud or options.humidity or options.wind or options.sunset or options.sunrise:
    print("Nothing chosen")





