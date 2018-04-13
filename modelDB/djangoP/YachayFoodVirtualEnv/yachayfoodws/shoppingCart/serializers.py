from rest_framework import serializers
from shoppingCart.models import ShoppingCart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'
