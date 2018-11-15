#!/usr/bin/python
import sys
import Adafruit_DHT
import argparse
import requests

from datetime import datetime

url = 'https://192.168.8.10:3080/intranet/weather/api/add.py'

sensor=Adafruit_DHT.DHT22 #if not using DHT22, replace with Adafruit_DHT.DHT11 or Adafruit_DHT.AM2302

parser = argparse.ArgumentParser(description='Read from DHT22 sensor')
parser.add_argument('--sensor', dest='sensor',
                   help='Defines the name of the sensor (default: null)')
parser.add_argument('--pin', dest='pin',
                   help='Defines the pin number (default: null)')
args = parser.parse_args()


def readdata():

    """
    Reads the data from sensor and calls the api to persist the data
    """

    humidity, temperature = Adafruit_DHT.read_retry(sensor, args.pin)#read_retry - retry getting temperatures for 15 times

    print("Temperature: %.1f C" % temperature)
    print("Humidity:    %.1f %%" % humidity)

    if humidity is not None and temperature is not None:
        # save data / call service
        data = {"data": """{"sensor-name": "%s", "temperature" : %s, "humidity": %s, "date": "%s"}""" % (args.sensor, temperature, humidity, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}

        response = requests.post(url, data=data, verify=False) # TODO: fixme

        sys.exit(response.status != 200)
    else:
        print("Failed to get reading. Try again!")
        sys.exit(1)


readdata()
