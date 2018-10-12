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

```
curl https://192.168.8.10:3080/intranet/weather/api/find.py?sensor=testsensor -k
```

## find recent

```
curl https://192.168.8.10:3080/intranet/weather/api/findrecent.py?sensor=testsensor -k
```
