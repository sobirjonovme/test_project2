from rest_framework import generics

from apps.task3.api_endpoints.product.ProductList.serializers import \
    ProductSerializer
from apps.task3.models import Product


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


__all__ = ["ProductListAPIView"]
