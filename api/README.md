# Enable python cgi in Apache Http-Server

Install and enable python-cgi

```
apt-get install python
a2enmod cgi
```

Add the following options:

```
<Directory /srv/www/yoursite/public_html>
    Options +ExecCGI
    AddHandler cgi-script .py
</Directory>
```

# Test API

## add new entry

```
curl https://192.168.8.10:3080/intranet/weather/api/add.py -k -d "data={\"temperature\": 31, \"humidity\": 51, \"date\": \"2018-10-12 19:21:14\", \"sensor-name\": \"testsensor\"}"
```
## find all

### required parameter

- sensor: name of the sensor
- from: minimum date
- to: maximum date

```
curl https://192.168.8.10:3080/intranet/weather/api/find.py?sensor=testsensor -k
```

## find recent

### required parameter

- sensor: name of the sensor

```
curl https://192.168.8.10:3080/intranet/weather/api/findrecent.py?sensor=testsensor -k
```

# Backends

## SQL

Tested with postgresql 9.6

To use sql backend use the following import:

`from _sqldb import SqlDBController as db`

## Influxdb

To use Influxdb backend use the following import:

`from _influxdb import InfluxDBController as db`
