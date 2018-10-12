#!/usr/bin/python

import cgi
import json

from _db import DBController as db

# Enable debug
#import cgitb
#cgitb.enable()

print("Content-Type: application/json;charset=utf-8")
print("")

# GET /apt/weather/findrecent?sensor=<name>
form = cgi.FieldStorage()
#   environ={'REQUEST_METHOD': 'GET'}
#)

# response data
# {
#  date: <current timestamp>,
#  sensor-name: <unique sensor name>,
#  temperature: <temp>,
#  humidity: <humidity>
# }
sensor = form.getvalue('sensor')

if sensor is None:
    print("{ error: No sensor supplied }")
else:
    print(json.dumps(db.getrecentvalue(sensor), sort_keys=True, default=str))
