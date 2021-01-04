from rest_framework import serializers
from customers import models

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customers
        fields = '__all__'