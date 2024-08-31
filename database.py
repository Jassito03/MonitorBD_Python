import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class Database:
    def __init__(self) -> None:
        self.username = config['DATABASE']['USERNAME']
        self.password = config['DATABASE']['PASSWORD']
        self.dns = config['DATABASE']['DNS']
        self.port = config['DATABASE']['PORT']
        self.encoding = config['DATABASE']['ENCODING']
