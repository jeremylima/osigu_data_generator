from elasticsearch import Elasticsearch
from config.Config import Config

config = Config
es = Elasticsearch(hosts=[config.ELASTIC_SEARCH], port=80, use_ssl=False)


class ElasticSearchClient:
    @staticmethod
    def post(doc):

        try:
            es.index(index="product", doc_type='product', id=doc['id'], body=doc)

        except Exception as e:
            print(e)
