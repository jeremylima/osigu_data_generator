import logging
from infrastructure.FileReader import FileReader
from infrastructure.ElasticSearchClient import ElasticSearchClient
from handlers.ProviderHandler import ProviderHandler
from handlers.InsurerHandler import InsurerHandler
from handlers.OsiguHandler import OsiguHandler
from utils.utils import print_progress

fileReader = FileReader('data//products.json')
products = fileReader.to_json()
elasticSearchClient = ElasticSearchClient
providerHandler = ProviderHandler
insurerHandler = InsurerHandler
osiguHandler = OsiguHandler


class ProductsHandler:
    @staticmethod
    def populate():
        i = 0
        total_items = len(products['products'])
        print_progress(i, total_items)
        for product in products['products']:
            osigu_product = product['osigu']
            elasticSearchClient.post(osigu_product)
            provider_products = providerHandler.create_product(osigu_product)
            insurer_products = insurerHandler.create_product(osigu_product)
            osiguHandler.associate_provider_product(osigu_product['id'], provider_products)
            osiguHandler.associate_insurer_product(osigu_product['id'], insurer_products)
            i += 1
            print_progress(i, total_items)
