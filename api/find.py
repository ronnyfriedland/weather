#!/usr/bin/python

import cgi
import json

from _influxdb import InfluxDBController as db

# Enable debug
#import cgitb
#cgitb.enable()

print("Content-Type: application/json;charset=utf-8")

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
    print("Status: 412 Precondition failed")
    print("")
    print("{ error: No sensor supplied }")
else:
    print("Status: 200 OK")
    print("")
    print(json.dumps(db.get_all_values(sensor, fromdate, todate), sort_keys=True, default=str))
