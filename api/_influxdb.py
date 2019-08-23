from influxdb import InfluxDBClient

import _config as config


class InfluxDBController:

    def __init__(self):
        pass

    @staticmethod
    def add_value(sensorname, date, temperature, humidity):
        """
        Writes a new entry with the given parameters into database
        :param sensorname: the name of the sensor - should be unique
        :type sensorname: str
        :param date: the datetime when the measure took place
        :type date: datetime.time
        :param temperature: the temperature value
        :type temperature: float
        :param humidity: the humidity value
        :type humidity: float
        """
        myConnection = None
        try:
            myConnection = InfluxDBController.openconnection()

            data = [
                {
                    "measurement": sensorname,
                    "time": int(date.timestamp()),
                    "fields": {
                        "temperature": temperature,
                        "humidity": humidity
                    }
                }
            ]

            myConnection.write_points(data, time_precision="u")
        except Exception as e:
            raise Exception("Error writing data", e)
        finally:
            InfluxDBController.closeconnection(myConnection)

    @staticmethod
    def get_recent_value(sensorname):
        """
        Retrieves the most recent record for the given sensor
        :param sensorname: the name of the sensor
        :type sensorname: str
        :return: the most recent data: array
        """
        myConnection = None
        try:
            myConnection = InfluxDBController.openconnection()
            rows = myConnection.query(
                "select time, temperature, humidity from " + sensorname + " order by time desc limit 1").get_points()
            for row in rows:
                result = {"sensor": sensorname, "measuredate": row['time'], "temperature": row['temperature'],
                          "humidity": row['humidity']}
                # result should contain only one result - so we can safely stop at this point
                break
        except Exception as e:
            raise Exception("Error reading data", e)
        finally:
            InfluxDBController.closeconnection(myConnection)

        return result

    @staticmethod
    def get_all_values(sensorname, fromdate, todate):
        """
        Retrieves all records for the given sensor
        :param sensorname: the name of the sensor
        :type sensorname: str
        :return: stored data for the given sensor
        """
        result = list()
        myConnection = None
        try:
            myConnection = InfluxDBController.openconnection()
            rows = myConnection.query("select time, temperature, humidity from " + sensorname + " where time >= " + str(
                int(fromdate.timestamp())) + " and time < " + str(int(todate.timestamp()))).get_points()
            for row in rows:
                result = {"sensor": sensorname, "measuredate": row['time'], "temperature": row['temperature'],
                          "humidity": row['humidity']}
        except Exception as e:
            raise Exception("Error reading data", e)
        finally:
            InfluxDBController.closeconnection(myConnection)

        return result

    @staticmethod
    def openconnection():
        """
        Opens a new database connection
        :return: the database connection
        """
        connection = InfluxDBClient(config.INFLUX_DATABASE_CONFIG['hostname'],
                                    config.INFLUX_DATABASE_CONFIG['port'],
                                    config.INFLUX_DATABASE_CONFIG['username'],
                                    config.INFLUX_DATABASE_CONFIG['password'],
                                    config.INFLUX_DATABASE_CONFIG['database'])

        connection.create_database(config.DATABASE_CONFIG['database'])

        return connection

    @staticmethod
    def closeconnection(connection):
        """
        Closes the given database connection (if initialized)
        :param connection: the connection to close
        """
        if connection is not None:
            connection.close()
