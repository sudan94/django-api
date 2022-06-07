from rest_framework import generics

from .models import Products
from .serializers import ProductsSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

# look up fild pk

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        # or None
        if description is None:
            description = title
        serializer.save(description=description)
        # can use signals in here didnot get much in this part perfrom_create
product_create_view = ProductCreateAPIView.as_view()


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


product_list_create_view = ProductListCreateAPIView.as_view()

"""
We can use list view instead of creat view as it will list and also allows creation endpoint 
"""
