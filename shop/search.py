from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Integer, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class ProductIndex(Document):
    brand = Text()
    model = Text()
    price = Integer()
    amount = Integer()
    category_id = Integer()

    class Index:
        name = 'product-index'


def bulk_indexing():
    ProductIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Product.objects.all().iterator()))


def search(model):
    es = Elasticsearch()
    s = es.search(index='product-index',body={"query": {"match": {"model": model}}})
    return s





