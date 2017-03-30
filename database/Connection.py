import psycopg2
from config.Config import Config

config = Config


class Connection:
    @staticmethod
    def get_connection():
        return psycopg2.connect(
            user=config.USER,
            password=config.PASSWORD,
            host=config.HOST,
            port=config.PORT,
            database=config.DATABASE
        )
