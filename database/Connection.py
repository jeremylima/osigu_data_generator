import psycopg2
from config import ConfigurationManager

config = ConfigurationManager


class Connection:
    @staticmethod
    def get_connection():
        return psycopg2.connect(
            user=config.get_database()['USER'],
            password=config.get_database()['PASSWORD'],
            host=config.get_database()['HOST'],
            port=config.get_database()['PORT'],
            database=config.get_database()['DATABASE']
        )
