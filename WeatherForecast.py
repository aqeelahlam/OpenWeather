import requests

from optparse import OptionParser
from datetime import datetime

parser = OptionParser()
parser.add_option('-api', action='store', dest='api_key',
                  help='An API token is required to perform the API request')

parser.add_option('-city', action='store', dest='city_name',
                  help='Perform query based on the name of the City')

parser.add_option('-cid', action='store', dest='city_id',
                  help='Perform query based on the name of the City ID')

parser.add_option('-gc', action='store', dest='geographic_coordinates',
                  help='Perform query based on the geographic coordinates given in latitude,longitude')

parser.add_option('-z', action='store', dest='zip_code',
                  help='Perform query based on the zip-code, country code')

parser.add_option('-time', action='store_true', dest='time',
                  help='This will display the current time at the given location')

parser.add_option('-pressure', action='store_true', dest='pressure',
                  help='This will display the current pressure(in Pa) at the given location')

parser.add_option('-cloud', action='store_true', dest='cloud',
                  help='This will display the current cloud conditions at the given location')

parser.add_option('-humidity', action='store_true', dest='humidity',
                  help='This will display the current humidity at the given location')

parser.add_option('-wind', action='store_true', dest='wind',
                  help='This will display the current wind speed at the given location')

parser.add_option('-sunset', action='store_true', dest='sunset',
                  help='This will display the current sunset time at the given location')

parser.add_option('-sunrise', action='store_true', dest='sunrise',
                  help='This will display the current sunrise time at the given location')

(options, args) = parser.parse_args()

