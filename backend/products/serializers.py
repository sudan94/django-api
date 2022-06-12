from rest_framework import serializers
from products.models import Products

class ProductsSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Products
        fields = ['id','title','description','price','sale_price','my_discount']

    def get_my_discount(self,obj):
        return obj.get_discount()

        # this is done just to change of the name of key from get_discount to my_discount other wise just passing the get_discount is enough