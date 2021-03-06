#!/usr/bin/python

import cgi
import json

from _influxdb import InfluxDBController as db

# Enable debug
# import cgitb
# cgitb.enable()

print("Content-Type: application/json;charset=utf-8")

# GET /weather/api/checkhumidity?sensor1=<name>&sensor2=<name>
form = cgi.FieldStorage()

# response data
# {
#  sensor1:
#  {
#    temperature: <value>,
#    humidity: <value>,
#  },
#  sensor2:
#  {
#    temperature: <value>,
#    humidity: <value>,
#  },
#  ok: <true|false>
# }
sensor1 = form.getvalue('sensor1')
sensor2 = form.getvalue('sensor2')


def handlePreconditionFailed(error):
    print("Status: 412 Precondition failed")
    print("")
    print(error)

if sensor1 is None:
    handlePreconditionFailed("{ error: No sensor1 supplied }")
elif sensor2 is None:
    handlePreconditionFailed("{ error: No sensor2 supplied }")
else:
    recent1 = db.get_recent_value(sensor1)
    recent2 = db.get_recent_value(sensor2)

    abs_sensor1 = (((0.000002 * pow(recent1['temperature'], 4)) + (0.0002 * pow(recent1['temperature'], 3)) + (
                0.0095 * pow(recent1['temperature'], 2)) + (0.337 * recent1['temperature']) + 4.9034) * recent1[
                             'humidity']) / 100

    abs_sensor2 = (((0.000002 * pow(recent2['temperature'], 4)) + (0.0002 * pow(recent2['temperature'], 3)) + (
                0.0095 * pow(recent2['temperature'], 2)) + (0.337 * recent2['temperature']) + 4.9034) * recent2[
                             'humidity']) / 100
    result = {sensor1: {"temperature": recent1["temperature"], "humidity": recent1["humidity"]},
              sensor2: {"temperature": recent2["temperature"], "humidity": recent2["humidity"]},
              "ok" : (abs_sensor2 < abs_sensor1)}

    print("Status: 200 OK")
    print("")
    print(json.dumps(result, sort_keys=True, default=str))
