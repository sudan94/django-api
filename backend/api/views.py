# from django.http import JsonResponse
from yaml import serialize
from products.models import Products
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductsSerializer

""" 
The *args keyword sends a list of values to a function. **kwargs sends a dictionary with values associated with keywords to a function.
Both of these keywords introduce more flexibility into your code. This is because you don’t have to specify a specific number of arguments upfront when writing a function.
"""

@api_view(['POST'])
def api_home(request,*args,**kwargs):
    """
    if request.method != 'POST':
        return Response({"message": "Use POST"},status=405)
        if rest framework is not used we have to manullay check the header 
    """
    # model_data = Products.objects.all().first()
    # instance = Products.objects.all().first()

    # print (instance)
    # data ={}
    # if instance:
    #     data = ProductsSerializer(instance).data
        # data['title'] = model_data.title
        # data['description'] = model_data.description
        # data['price'] = model_data.price  
        # data = model_to_dict(model_data, fields=['title','description','price'])

    serializers = ProductsSerializer(data=request.data)
    if(serializers.is_valid(raise_exception=True)):
        instance = serializers.save()
        print(instance)
        return Response(serializers.data)
    # return Response(data)


    """
    The process of calling a end point using django restframeworks is as follows:
    1. First endpint hit the cfehome urls.py
    2. Then it hits the api urls.py
    3. Then it hits the api_home function
    4. Then api_home function will call the respective function on serializers.py
    5. Then the function in serializers.py will call the respective model
    6. Then serializers.py retuns the data to api_home function
    7. check if serializers is valid in api_home function
    8. if valid then save/delete/get/update the data else return the error

    """