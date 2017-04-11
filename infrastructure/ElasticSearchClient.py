from elasticsearch import Elasticsearch
from config import ConfigurationManager

config = ConfigurationManager
es = Elasticsearch(hosts=[config.get_elastic_search_host()], port=80, use_ssl=False)


class ElasticSearchClient:
    @staticmethod
    def post(index, doc_id, body):

        try:
            es.index(index=index, doc_type=index, id=doc_id, body=body)

        except Exception as e:
            print(e)
