#!/usr/bin/python

import cgi
import json

from _db import DBController as db

# Enable debug
#import cgitb
#cgitb.enable()

print("Content-Type: application/json;charset=utf-8")
print("")

# GET /weather/api/find?sensor=<name>
form = cgi.FieldStorage()

# response data
# [{
#  date: <current timestamp>,
#  sensor-name: <unique sensor name>,
#  temperature: <temp>,
#  humidity: <humidity>
# }]
sensor = form.getvalue('sensor')
fromdate = form.getvalue('from')
todate = form.getvalue('to')

if sensor is None:
    print("{ error: No sensor supplied }")
else:
    print(json.dumps(db.getallvalues(sensor, fromdate, todate), sort_keys=True, default=str))
