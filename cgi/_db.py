#!/usr/bin/python

import psycopg2

import _config as config


class DBController:
    """
    create table temperatures(
        id serial PRIMARY KEY,
        creationdate timestamp NOT NULL,
        sensor text NOT NULL,
        measuredate timestamp NOT NULL,
        temperature float NOT NULL,
        humidity float NOT NULL
        );
    """

    def __init__(self):
        pass

    @staticmethod
    def addvalue(sensorname, date, temperature, humidity):
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
            myConnection = DBController.openconnection()
            cur = myConnection.cursor()
            cur.execute(
                """
                    insert into temperatures (creationdate, sensor, measuredate, temperature, humidity) 
                    values (now(), %s, %s, %s, %s)
                """, (
                    sensorname, date, float(temperature), float(humidity)))
            myConnection.commit()
        except Exception as e:
            raise Exception("Error writing data", e)
        finally:
            DBController.closeconnection(myConnection)

    @staticmethod
    def getrecentvalue(sensorname):
        """
        Retrieves the most recent record for the given sensor
        :param sensorname: the name of the sensor
        :type sensorname: str
        :return: the most recent data: array
        """
        myConnection = None
        try:
            myConnection = DBController.openconnection()
            cur = myConnection.cursor()
            cur.execute(
                """
                    select distinct on (sensor) sensor, measuredate, temperature, humidity from temperatures
                    where sensor = %s order by sensor, measuredate desc
                """, (sensorname,))
            row = cur.fetchone()
            result = {"sensor": row[0], "measuredate": row[1], "temperature": row[2], "humidity": row[3]}
        except Exception as e:
            raise Exception("Error reading data", e)
        finally:
            DBController.closeconnection(myConnection)

        return result

    @staticmethod
    def getallvalues(sensorname):
        """
        Retrieves all records for the given sensor
        :param sensorname: the name of the sensor
        :type sensorname: str
        :return: stored data for the given sensor
        """
        result = list()
        myConnection = None
        try:
            myConnection = DBController.openconnection()
            cur = myConnection.cursor()
            cur.execute(
                """
                    select sensor, measuredate, temperature, humidity from temperatures 
                    where sensor = %s order by measuredate desc
                """, (sensorname,))
            rows = cur.fetchall()
            for row in rows:
                result.append({"sensor": row[0], "measuredate": row[1], "temperature": row[2], "humidity": row[3]})
        except Exception as e:
            raise Exception("Error reading data", e)
        finally:
            DBController.closeconnection(myConnection)

        return result

    @staticmethod
    def openconnection():
        """
        Opens a new database connection
        :return: the database connection
        """
        connection = psycopg2.connect(host=config.DATABASE_CONFIG['hostname'],
                                      port=config.DATABASE_CONFIG['port'],
                                      user=config.DATABASE_CONFIG['username'],
                                      password=config.DATABASE_CONFIG['password'],
                                      dbname=config.DATABASE_CONFIG['database'],
                                      sslmode=config.DATABASE_CONFIG['sslmode'])
        return connection

    @staticmethod
    def closeconnection(connection):
        """
        Closes the given database connection (if initialized)
        :param connection: the connection to close
        """
        if connection is not None:
            connection.close()
