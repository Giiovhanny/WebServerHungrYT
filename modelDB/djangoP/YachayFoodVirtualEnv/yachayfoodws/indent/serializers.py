from rest_framework import serializers
from indent.models import Indent

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indent
        fields = '__all__'
