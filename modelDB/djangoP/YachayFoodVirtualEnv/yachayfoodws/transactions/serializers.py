from rest_framework import serializers
from transactions.models import Transactions

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
