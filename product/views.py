#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from product.models import Product
from product.serializers import ProductSerializer
# Create your views here.
@csrf_exempt
def product_list(request):
    """
    List all code products, or create a product.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PorductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def delete(request, id):
    try:
        product = Product.objects.get(pk=id)
        product.delete()
        return HttpResponse('deleted')
    except Product.DoesNotExist:
        return HttpResponse(status=404)    


