from rest_framework import serializers
from deliveryProduct.models import DeliveryProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryProduct
        fields = '__all__'
