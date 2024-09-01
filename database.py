import configparser
import cx_Oracle
import os
import sys
import os

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

    def consulta_reads(self):
        if self.connection is None:
            print("La conexión no está establecida.")
            return

        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM ALUMNO"
            cursor.execute(query)
            tablas = cursor.fetchall()
            for tabla in tablas:
                print(tabla[0])
            cursor.close()
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ejecutar la consulta: {e}")


myDB = Database()
myDB.establecer_conexion()
myDB.consulta_reads()
