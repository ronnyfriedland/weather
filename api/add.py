#!/usr/bin/python

import cgi
import json

from _influxdb import InfluxDBController as db
from datetime import datetime

# Enable debug
#import cgitb
#cgitb.enable()

print("Content-Type: application/json;charset=utf-8")

# POST /weather/api/add
form = cgi.FieldStorage()
#    environ={'REQUEST_METHOD': 'POST'}

# Get data from request
# {
#  date: <current timestamp>,
#  sensor-name: <unique sensor name>,
#  temperature: <temperature>,
#  humidity: <humidity>
# }

data = json.loads(form.getvalue('data'))
#json_string = """
# {
#  "date": \"""" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """\",
#  "sensor-name": "testsensor",
#  "temperature": "21",
#  "humidity": "66.6"
# }"""

date = data['date']
sensorName = data['sensor-name']
temperature = data['temperature']
humidity = data['humidity']

def handlePreconditionFailed(error):
    print("Status: 412 Precondition failed")
    print("")
    print(error)


# validate
if date is None:
    handlePreconditionFailed("{ error: No date supplied }")
if sensorName is None:
    handlePreconditionFailed("{ error: No sensor name supplied }")
if temperature is None:
    handlePreconditionFailed("{ error: No temperature supplied }")
if humidity is None:
    handlePreconditionFailed("{ error: No humidity supplied }")

# persist
db.add_value(sensorName, datetime.strptime(date, "%Y-%m-%d %H:%M:%S"), temperature, humidity)

print("Status: 201 Created")
print("")
