import requests
import argparse
from datetime import datetime
import sys

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


def options():
    """

    :return:
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('-api', action='append', dest='api_key',
                        help='An API token is required to perform the API request')

    parser.add_argument('-city', action='append', dest='city_name',
                        help='Perform query based on the name of the City')

    parser.add_argument('-cid', action='append', dest='city_id',
                        help='Perform query based on the name of the City ID')

    parser.add_argument('-gc', action='append', dest='geographic_coordinates',
                        help='Perform query based on the geographic coordinates given in latitude,longitude')

    parser.add_argument('-z', action='append', dest='zip_code',
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


def print_information(response, options):
    """
    This function is used to print out the results to the console.
    :param response: This parameter holds the response from the website in JSON format.
    :return: Prints a message onto console based on input given in by the user.

    The 'format' function was used to convert the float number to 2 significant figures.
    """
    # This variable holds all the information in JSON format that is
    apiData = response.json()

    if options.temperature:
        if str(options.temperature).lower() == 'celsius':
            celsiusMin = int(apiData['main']['temp_min']) - 273.15
            celsiusMax = int(apiData['main']['temp_max']) - 273.15
            print("The temperature ranges from", format(celsiusMin, '.2f'),
                  "-", format(celsiusMax, '.2f'), "celsius")

        elif str(options.temperature).lower() == 'fahrenheit':
            fahrenheitMin = (int(apiData['main']['temp_min']) * 9 / 5) - 459.67
            fahrenheitMax = (int(apiData['main']['temp_max']) * 9 / 5) - 459.67

            print("The temperature ranges from", format(fahrenheitMin, '.2f'),
                  "-", format(fahrenheitMax, '.2f'), "fahrenheit")

        else:
            print("Invalid unit type for temperature")

    if options.time:
        timeStamp = int(apiData['dt'])
        currentTime = datetime.utcfromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')
        print("On", currentTime)

    if options.pressure:
        print("The atmospheric pressure at this locality is at", str(apiData['main']['pressure']) + "Pa")

    if options.cloud:
        print("Cloudiness:", str(apiData['clouds']['all']), "%")

    if options.humidity:
        print("It is likely Cloudy with a humidity of", str(apiData['main']['humidity']) + "%")

    if options.wind:
        print("There is wind speed", str(apiData['wind']['speed']), "meter/sec from", str(apiData['wind']['deg']),
              "degrees")

    if options.sunset:
        sunsetTimeStamp = int(apiData['sys']['sunset'])
        sunsetTime = datetime.utcfromtimestamp(sunsetTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
        print("The sun will set at", sunsetTime)

    if options.sunrise:
        sunriseTimeStamp = int(apiData['sys']['sunrise'])
        sunriseTime = datetime.utcfromtimestamp(sunriseTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
        print("The sun will rise at", sunriseTime)


def multiple_locations(options):
    """
    This function is used to return True or False based on whether or not the user chooses multiple locations.
    :return: Returns True if only one of the location tokens have been used at a given time.
    True: If only one location type is chosen.
    False: If more than one type was chosen.
    """

    if options.city_name and (options.city_id or
                              options.geographic_coordinates or options.zip_code):
        return True

    elif options.city_id and (options.city_name or
                              options.geographic_coordinates or options.zip_code):
        return True

    elif options.geographic_coordinates and (options.city_name or
                                             options.city_id or options.zip_code):
        return True

    elif options.zip_code and (options.city_name or
                               options.city_id or options.geographic_coordinates):
        return True

    else:
        return False


def infeasible_cases(options):
    """
    This function is used to return True or False based on whether or not an infeasible situation has occurred.
    This includes no inputs, and multiple of the same input.
    :return: Returns True if only an infeasible situation occurs.
    True: If only one location type is chosen.
    False: If more than one type was chosen.
    """
    # if no options are given
    if len(sys.argv) == 1:
        print("No inputs were given")
        return "No inputs were given"

    if not options.api_key:
        print("No api token given")
        return "No api token given"

    if not(options.city_name or options.city_id or options.geographic_coordinates or options.zip_code):
        print("No Location input given")
        return "No location input given"

    # For repeated arguments
    for x in range(len(sys.argv)):
        for y in range(x+1, len(sys.argv)):
            if sys.argv[x] == sys.argv[y]:
                print("Input argument " + str(y+1) + " is a repeat argument")
                return True

    if len(options.api_key) != 1:
        print(len(options.api_key))
        print("Multiple api keys given")
        return True
    else:
        options.api_key = options.api_key[0]

    if options.city_name:
        if len(options.city_name) == 1:
            options.city_name = options.city_name[0]
        else:
            print("Multiple cities given")
            return True

    elif options.city_id:
        if len(options.city_id) == 1:
            options.city_id = options.city_id[0]
        else:
            print("Multiple cities given")
            return True

    elif options.zip_code:
        if len(options.zip_code) == 1:
            options.zip_code = options.zip_code[0]
        else:
            print("Multiple cities given")
            return True

    elif options.geographic_coordinates:
        if len(options.geographic_coordinates) == 1:
            options.geographic_coordinates = options.geographic_coordinates[0]
        else:
            print("Multiple cities given")
            return True

    return False


def api_token_input(options):
    """

    :return:
    """

    otherTokens = options.time or options.pressure or options.cloud \
                  or options.humidity or options.wind or options.sunset \
                  or options.sunrise or options.temperature

    if multiple_locations(options):
        print("Multiple chosen location types are specified")
        return "Multiple chosen location types are specified"

    # elif infeasible_cases(options):
    #     return

    else:
        try:
            # This is for when the user chooses to get information using the tokens based on the City Name
            if options.api_key and options.city_name and otherTokens:
                url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
                response = requests.get(url.format(options.city_name, options.api_key))
                return print_information(response, options)

            # This is for when the user chooses to get information using the tokens based on the City ID
            elif options.api_key and options.city_id and otherTokens:
                url = "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}"
                response = requests.get(url.format(options.city_id, options.api_key))
                return print_information(response, options)

            # This is for when the user chooses to get information using the tokens based on the Geographic Coordinates
            elif options.api_key and options.geographic_coordinates and otherTokens:
                GeoCoordinates = options.geographic_coordinates.split(",")
                latitude = GeoCoordinates[0]
                longitude = GeoCoordinates[1]
                url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"
                response = requests.get(url.format(latitude, longitude, options.api_key))
                return print_information(response, options)

            # This is for when the user chooses to get information using the tokens based on the Zip Code
            elif options.api_key and options.zip_code and otherTokens:
                url = "https://api.openweathermap.org/data/2.5/weather?zip={}&appid={}"
                response = requests.get(url.format(options.zip_code, options.api_key))
                return print_information(response, options)

            # If the user doesn't specify any tokens
            elif not otherTokens:
                print("There is no chosen information (e.g., time or temperature)")
                return "There is no chosen information (e.g., time or temperature)"

        except KeyError:
            print("Either API or Location Tokens are invalid.")
            return "Either API or Location Tokens are invalid."


if __name__ == "__main__":
    api_token_input(options())




