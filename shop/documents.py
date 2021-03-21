from django_elasticsearch_dsl import DocType, Index
from .models import Product

posts=Index('prodicts')

@posts.doc_type
class   PostDocument(DocType):
    model = Product

    fields = [
        'id',
        'brand',
        'model',
        'price',
        'amount',
        'category_id'
    ]