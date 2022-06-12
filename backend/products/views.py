from rest_framework import generics, mixins

from .models import Products
from .serializers import ProductsSerializer


class ProductMixinView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    def get(self,request, pk=None, *args, **kwargs):
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args, **kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def put(self,request,pk,*args,**kwargs):
        queryset = Products.objects.get(pk=pk)
        serializer_class = ProductsSerializer   
        return self.update(request,*args,**kwargs)

    def delete(self,request,pk,*args,**kwargs):
        queryset = Products.objects.get(pk=pk)
        return self.destroy(request,*args,**kwargs)

"""
look into details about   if serializer.is_valid():
            serializer.save()
"""



product_mixin_view = ProductMixinView.as_view()

# look for the primary key detail of 1 element
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

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductDestroyAPIVIew(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIVIew.as_view()

"""
We can use list view instead of creat view as it will list and also allows creation endpoint 

Another point : function based views can also be done but its not recommended as we have to make form scratch and looks confusing (use in special cases)
"""
