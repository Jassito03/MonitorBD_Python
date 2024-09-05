"""
Autores:
Nombre: Joseph Piñar Baltodano
ID: 1 1890 0308

Nombre: Abigail Salas Ramírez
ID: 4 0257 0890

Nombre: Gianpablo Moreno Castro
ID: 4 0261 0240
"""


import configparser
import cx_Oracle
import pandas as pd

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
            self.connection = cx_Oracle.connect(
                user=self._username, 
                password=self._password, 
                dsn=dns, 
                encoding=self._encoding,
                mode=cx_Oracle.SYSDBA
            )
            print("Conexión exitosa")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al conectar a la base de datos: {e}")
            traceback.print_exc()

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
            query = "SELECT value FROM V$SYSSTAT WHERE name = 'db block gets'"
            cursor.execute(query)
            tablas = cursor.fetchall()
            cursor.close()
            return tablas[0][0]
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ejecutar la consulta total de lecturas fisicas: {e}")

    def total_lecturas_logicas(self):
        if self.connection is None:
            print("La conexión no está establecida.")
            return
        try:
            cursor = self.connection.cursor()
            query = "SELECT value FROM V$SYSSTAT WHERE name = 'consistent gets'"
            cursor.execute(query)
            tablas = cursor.fetchall()
            cursor.close()
            return tablas[0][0]
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ejecutar la consulta total de lecturas logicas: {e}")

    def estructura_fisica(self):
        if self.connection is None:
            print("La conexión no está establecida.")
            return
        try:
            cursor = self.connection.cursor()
            query = "SELECT l.status AS estado, f.member AS nombre_archivo FROM v$log l JOIN v$logfile f ON l.group# = f.group# ORDER BY l.group#;"
            cursor.execute(query)
            estados = cursor.fetchall()
            cursor.close()
            return estados
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ejecutar la consulta total de lecturas logicas: {e}")
