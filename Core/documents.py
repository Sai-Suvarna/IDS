from django_elasticsearch_dsl import Document, fields, Index
from Core.models import IDSProductDetails


# Define Elasticsearch index
product_index = Index('products')

@product_index.doc_type
class IDSProductDetailsDocument(Document):
    images = fields.TextField()

    class Django:
        model = IDSProductDetails  # Django model to map

        # Define fields to be indexed
        fields = [
            'productId',
            'category',
            'item',
            'description',
            'units',
            'thresholdValue',
        ]

