from rest_framework import generics

from .models import Products
from .serializers import ProductsSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

# look up fild pk

