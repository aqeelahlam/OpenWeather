import requests
import argparse
from datetime import datetime


"""
For action:

The action has two different options that I have used, store and store_true

store: Requires an  argument to be inserted through the command lined
store_true: This doesnt require an argument
 
"""


"""
For dest:

This is the name of the token
"""

def options_tokens():
    """

    :return:
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('-api', action='store', dest='api_key',
                        help='An API token is required to perform the API request')

    parser.add_argument('-city', action='store', dest='city_name',
                        help='Perform query based on the name of the City')

    parser.add_argument('-cid', action='store', dest='city_id',
                        help='Perform query based on the name of the City ID')

    parser.add_argument('-gc', action='store', dest='geographic_coordinates',
                        help='Perform query based on the geographic coordinates given in latitude,longitude')

    parser.add_argument('-z', action='store', dest='zip_code',
                        help='Perform query based on the zip-code, country code')

    parser.add_argument('-time', action='store_true', dest='time',
                        help='This will display the current time at the given location')

    parser.add_argument('-temp', action='store', nargs='?', const='celsius', dest='temperature',
                        help='This will give us the temperature in celsius')

    parser.add_argument('-pressure', action='store_true', dest='pressure',
                        help='This will display the current pressure(in Pa) at the given location')

    parser.add_argument('-cloud', action='store_true', dest='cloud',
                        help='This will display the current cloud conditions at the given location')

    parser.add_argument('-humidity', action='store_true', dest='humidity',
                        help='This will display the current humidity at the given location')

    parser.add_argument('-wind', action='store_true', dest='wind',
                        help='This will display the current wind speed at the given location')

    parser.add_argument('-sunset', action='store_true', dest='sunset',
                        help='This will display the current sunset time at the given location')

    parser.add_argument('-sunrise', action='store_true', dest='sunrise',
                        help='This will display the current sunrise time at the given location')

    options = parser.parse_args()


    return options


def print_information(response):
    """
    This function is used to print out the results to the console.
    :param response: This parameter holds the response from the website in JSON format.
    :return: Prints a message onto console based on input given in by the user.

    The 'format' function was used to convert the float number to 2 significant figures.
    """
    # This variable holds all the information in JSON format that is
    apiData = response.json()

    if options_tokens().temperature:
        if str(options_tokens().temperature) == 'celsius':
            celsiusMin = int(apiData['main']['temp_min']) - 273.15
            celsiusMax = int(apiData['main']['temp_max']) - 273.15
            print("The temperature ranges from", format(celsiusMin, '.2f'),
                  "-", format(celsiusMax, '.2f'), "celsius")

        elif str(options_tokens().temperature) == 'fahrenheit':
            fahrenheitMin = (int(apiData['main']['temp_min']) * 9/5) - 459.67
            fahrenheitMax = (int(apiData['main']['temp_max']) * 9/5) - 459.67

            print("the temperature ranges from", format(fahrenheitMin, '.2f'),
                  "-", format(fahrenheitMax, '.2f'), "fahrenheit")

        else:
            print("Invalid unit type for temperature")

    if options_tokens().time:
        timeStamp = int(apiData['dt'])
        currentTime = datetime.utcfromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')
        print("On", currentTime)

    if options_tokens().pressure:
        print("The atmospheric pressure at this locality is at", str(apiData['main']['pressure'])+"Pa")

    if options_tokens().cloud:
        print("Cloudiness:", str(apiData['clouds']['all']), "%")

    if options_tokens().humidity:
        print("It is likely Cloudy with a humidity of", str(apiData['main']['humidity'])+"%")

    if options_tokens().wind:
        print("There is wind speed", str(apiData['wind']['speed']), "meter/sec from", str(apiData['wind']['deg']), "degrees")

    if options_tokens().sunset:
        sunsetTimeStamp = int(apiData['sys']['sunset'])
        sunsetTime = datetime.utcfromtimestamp(sunsetTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
        print("The sun will set at", sunsetTime)

    if options_tokens().sunrise:
        sunriseTimeStamp = int(apiData['sys']['sunrise'])
        sunriseTime = datetime.utcfromtimestamp(sunriseTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
        print("The sun will rise at", sunriseTime)


def multiple_locations():
    """
    This function is used to return True or False based on whether or not the user chooses multiple locations.
    :return: Returns True if only one of the location tokens have been used at a given time.
    True: If only one location type is chosen.
    False: If more than one type was chosen.
    """

    if options_tokens().city_name and (options_tokens().city_id or
                                       options_tokens().geographic_coordinates or options_tokens().zip_code):
        return True

    elif options_tokens().city_id and (options_tokens().city_name or
                                       options_tokens().geographic_coordinates or options_tokens().zip_code):
        return True

    elif options_tokens().geographic_coordinates and (options_tokens().city_name or
                                                      options_tokens().city_id or options_tokens().zip_code):
        return True

    elif options_tokens().zip_code and (options_tokens().city_name or
                                        options_tokens().city_id or options_tokens().geographic_coordinates):
        return True

    else:
        return False


def api_token_input():
    """

    :return:
    """

    otherTokens = options_tokens().time or options_tokens().pressure or options_tokens().cloud\
           or options_tokens().humidity or options_tokens().wind or options_tokens().sunset\
           or options_tokens().sunrise or options_tokens().temperature

    if multiple_locations():
        print("Multiple chosen locations are specified")
    else:

        # This is for when the user chooses to get information using the tokens based on the City Name
        if options_tokens().api_key and options_tokens().city_name and otherTokens:
            url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
            response = requests.get(url.format(options_tokens().city_name, options_tokens().api_key))
            print(url.format(options_tokens().city_name, options_tokens().api_key))
            print_information(response)

        # This is for when the user chooses to get information using the tokens based on the City ID
        elif options_tokens().api_key and options_tokens().city_id and otherTokens:
            url = "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}"
            response = requests.get(url.format(options_tokens().city_id, options_tokens().api_key))
            print_information(response)

        # This is for when the user chooses to get information using the tokens based on the Geographic Coordinates
        elif options_tokens().api_key and options_tokens().geographic_coordinates and otherTokens:
            GeoCoordinates = options_tokens().geographic_coordinates.split(",")
            latitude = GeoCoordinates[0]
            longitude = GeoCoordinates[1]
            url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"
            response = requests.get(url.format(latitude, longitude, options_tokens().api_key))
            print_information(response)

        # This is for when the user chooses to get information using the tokens based on the Zip Code
        elif options_tokens().api_key and options_tokens().zip_code and otherTokens:
            url = "https://api.openweathermap.org/data/2.5/weather?zip={}&appid={}"
            response = requests.get(url.format(options_tokens().zip_code, options_tokens().api_key))
            print_information(response)

        # If the user doesn't specify any tokens
        elif not otherTokens:
            print("There is no chosen information (e.g., time or temperature)")


if __name__ == "__main__":
    api_token_input()

##08fce8ac44b0fe40a029e7d1a0b987a2
