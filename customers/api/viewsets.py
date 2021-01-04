from rest_framework import viewsets
from customers.api import serializers
from customers import models

class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomersSerializer
    queryset = models.Customers.objects.all()