from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        #fields = ('id_product', 'id_seller', 'name', 'description', 'precio_unitario', 'stock', 'delivery_date', 'limit_date', 'register_date', 'id_category')
        fields = '__all__'

