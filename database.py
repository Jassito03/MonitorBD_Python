import configparser
import cx_Oracle

config = configparser.ConfigParser()
config.read('config.ini')

class Database:
    """Class Database"""
    def __init__(self) -> None:
        self._username = config['DATABASE']['USERNAME']
        self._password = config['DATABASE']['PASSWORD']
        self._url = config['DATABASE']['URL']
        self._port = config['DATABASE']['PORT']
        self._service_name = config['DATABASE']['SERVICE_NAME']
        self._encoding = config['DATABASE']['ENCODING']
        self.connection = any

    def establecer_conexion(self):
        """Método para iniciar la conexión con la BD"""
        dns = cx_Oracle.makedns(self._url, self._port, self._service_name)
        self.connection = cx_Oracle.connect(user=self._username, password=self._password, dns=dns, encoding=self._encoding, mode=cx_Oracle.SYSDBA)
