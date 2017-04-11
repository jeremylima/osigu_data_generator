import requests
import sys
from database.Connection import Connection
from config import ConfigurationManager
from infrastructure.FileReader import FileReader
from handlers.DatabaseHandler import DatabaseHandler

conn = Connection
config = ConfigurationManager
dbHandler = DatabaseHandler


def clean_database():
    file_reader = FileReader('database/scripts/cleaner.sql')
    statements = file_reader.read().split(';')
    statements = list(filter(None, statements))
    dbHandler.execute_multiple_statements(statements)
    print('Database cleaned successfully')


def clean_products_from_elasticsearch():
    delete_from_elasticsearch('product')
    print('Products deleted successfully from elasticsearch')


def clean_diagnoses_from_elasticsearch():
    delete_from_elasticsearch('diagnoses')
    print('Diagnoses deleted successfully from elasticsearch')


def delete_from_elasticsearch(index):
    url = config.get_elastic_search_host() + '/{index}/_query?q={query}'.format(index=index, query="QA TESTING")
    resp = requests.delete(url)

    assert resp.status_code == 200, "An error occurs when deleting elasticsearch {index}. {error}" \
        .format(index=index, error=resp.text)


class CleanerHandler:
    @staticmethod
    def clean():
        clean_database()
        clean_products_from_elasticsearch()
        clean_diagnoses_from_elasticsearch()
