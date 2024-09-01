import configparser
import cx_Oracle
import os
import sys
import plotly.express as px


config = configparser.ConfigParser()
config.read('config.ini')


instance_client = config['DATABASE']['INSTANCE_CLIENT']
cx_Oracle.init_oracle_client(lib_dir = instance_client)

class Database:
    """Class Database"""
    def __init__(self) -> None:
        self._username = config['DATABASE']['USERNAME']
        self._password = config['DATABASE']['PASSWORD']
        self._url = config['DATABASE']['URL']
        self._port = config['DATABASE']['PORT']
        self._service_name = config['DATABASE']['SERVICE_NAME']
        self._encoding = config['DATABASE']['ENCODING']
        self.connection = None

    def establecer_conexion(self):
        """Método para iniciar la conexión con la BD"""
        try:
            dns = cx_Oracle.makedsn(self._url, self._port, service_name=self._service_name)
            self.connection = cx_Oracle.connect(user=self._username, password=self._password, dsn=dns, encoding=self._encoding, mode=cx_Oracle.SYSDBA)
            print("Conexión exitosa")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al conectar a la base de datos: {e}")

    def tasa_de_hit(self):
        if self.connection is None:
            print("La conexión no está establecida")
            return
        try:
            cursor = self.connection.cursor()
            query = ("SELECT" 
            "(1 - (physical_reads.value / logical_reads.value)) * 100 AS \"Tasa de Hit del Buffer Cache (%)\" "
            "FROM (SELECT value FROM V$SYSSTAT WHERE name = 'db block gets') physical_reads, "
            "(SELECT value FROM V$SYSSTAT WHERE name = 'consistent gets') logical_reads")
            cursor.execute(query)
            tablas = cursor.fetchall()
            
            for tabla in tablas:
                total = tabla[0]
                porcentaje = f"{total:.2f}"
                print(porcentaje)
            cursor.close()
            return porcentaje
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ejecutar la consulta tasa de hits: {e}")
        
    def total_lecturas_fisicas(self):
        if self.connection is None:
            print("La conexión no está establecida.")
            return

        try:
            cursor = self.connection.cursor()
            query = "SELECT name, value FROM V$SYSSTAT WHERE name IN ('physical writes')"
            cursor.execute(query)
            tablas = cursor.fetchall()
            total = 0
            for tabla in tablas:
                total = tabla[1]
            cursor.close()
            return total
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ejecutar la consulta total de lecturas fisicas: {e}")

    def total_lecturas_logicas(self):
        if self.connection is None:
            print("La conexión no está establecida.")
            return

        try:
            cursor = self.connection.cursor()
            query = "SELECT name, value FROM V$SYSSTAT WHERE name IN ('db block changes');"
            cursor.execute(query)
            tablas = cursor.fetchall()
            total = 0
            for tabla in tablas:
                total = tabla[1]
            cursor.close()
            return total
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ejecutar la consulta total de lecturas logicas: {e}")


myDB = Database()
myDB.establecer_conexion()
myDB.total_lecturas_fisicas()
myDB.tasa_de_hit()