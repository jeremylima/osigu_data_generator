from elasticsearch import Elasticsearch
from config import ConfigurationManager

config = ConfigurationManager
es = Elasticsearch(hosts=[config.get_elastic_search_host()], port=80, use_ssl=False)


class ElasticSearchClient:
    @staticmethod
    def post(doc):

        doc['full_name'] += ' - QA TESTING'
        try:
            es.index(index="product", doc_type='product', id=doc['id'], body=doc)

        except Exception as e:
            print(e)
