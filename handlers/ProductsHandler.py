import logging
from infrastructure.FileReader import FileReader
from infrastructure.ElasticSearchClient import ElasticSearchClient
from handlers.ProviderHandler import ProviderHandler
from handlers.InsurerHandler import InsurerHandler
from handlers.OsiguHandler import OsiguHandler
from handlers.PbmHandler import PbmHandler
from utils.utils import print_progress, print_json

fileReader = FileReader('data//products.json')
products = fileReader.to_json()
elasticSearchClient = ElasticSearchClient
providerHandler = ProviderHandler
insurerHandler = InsurerHandler
osiguHandler = OsiguHandler
pbmHandler = PbmHandler()


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

            if 'associate_provider' not in product:
                osiguHandler.associate_provider_product(osigu_product['id'], provider_products)

            if 'associate_insurer' not in product:
                osiguHandler.associate_insurer_product(osigu_product['id'], insurer_products)

            if 'pbm' in product:
                pbmHandler.build_product_categories_statement(product)
                if 'substitute_osigu_product_id' in product['pbm']:
                    pbmHandler.build_substitute_products_statement(product)

            i += 1
            print_progress(i, total_items)

        pbmHandler.populate()
