#!/usr/bin/python

import cgi
import json

from _db import DBController as db
from datetime import datetime

# Enable debug
#import cgitb
#cgitb.enable()

print("Content-Type: application/json;charset=utf-8")
print("")

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

# validate
if date is None:
    print("{ error: No date supplied }")
if sensorName is None:
    print("{ error: No sensor name supplied }")
if temperature is None:
    print("{ error: No temperature supplied }")
if humidity is None:
    print("{ error: No humidity supplied }")

# persist
db.addvalue(sensorName, datetime.strptime(date, "%Y-%m-%d %H:%M:%S"), temperature, humidity)
