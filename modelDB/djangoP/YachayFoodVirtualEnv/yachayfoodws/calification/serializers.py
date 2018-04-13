from rest_framework import serializers
from calification.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calification
        fields = '__all__'
