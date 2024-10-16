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
        """
        Inicialización de la clase para obtener la información 
        ingresada desde el archivo config.ini
        """
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
        """Método para calcular la tasa de hits"""
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
        """Método para obtener el total de lecturas físicas"""
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
        """Método para obtener el total de lecturas lógicas"""
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

    def calculo_tablespaces(self):
        """
        Método para obtener la información de los tablespaces, tales como:
        el nombre, el tamaño total, total de la memoria libre y total de lamemoria usada        
        """
        if self.connection is None:
            print("La conexión no está establecida.")
            return
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT a.tablespace_name,
                b.size_kb / 1024 AS SIZE_MB,
                a.free_kb / 1024 AS FREE_MB,
                (b.size_kb - a.free_kb) / 1024 AS USED_MB
            FROM (SELECT tablespace_name,
                        TRUNC(SUM(bytes) / 1024) AS free_kb
                FROM dba_free_space
                GROUP BY tablespace_name) a,
                (SELECT tablespace_name,
                        TRUNC(SUM(bytes) / 1024) AS size_kb
                FROM dba_data_files
                GROUP BY tablespace_name) b
            WHERE a.tablespace_name = b.tablespace_name
            """
            cursor.execute(query)
            tablas = cursor.fetchall()
            df = pd.DataFrame(tablas, columns=['Nombres', 'Tamanio Total', 'Memoria Libre', 'Memoria Usada'])
            cursor.close()
            return df
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ejecutar la consulta del tamaño total de los tablespaces: {e}")

    def bitacoras(self):
        """
        Método para obtener la información de los archivos Redo Logs, tales como:
        El estado del archivo (Current/Inactive), el nombre y el tamaño total en Bytes
        """
        if self.connection is None:
            print("La conexión no está establecida.")
            return
        try:
            cursor = self.connection.cursor()
            query = "SELECT l.status AS estado, f.member AS nombre_archivo, l.bytes as tamanio_bytes FROM v$log l JOIN v$logfile f ON l.group# = f.group# ORDER BY l.group#"
            cursor.execute(query)
            estados = cursor.fetchall()
            df = pd.DataFrame(estados, columns=['Estado', 'Nombre', 'bytes'])
            cursor.close()
            return df
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ejecutar la consulta total de lecturas logicas: {e}")

    def switch_logfile(self):
        if self.connection is None:
            print("La conexión no está establecida")
            return
        try:
            cursor = self.connection.cursor()
            query = "ALTER SYSTEM SWITCH LOGFILE"
            cursor.execute(query)
            cursor.close()
            return
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ejecutar la consulta para hacer switch del logfile actual: {e}")