from django.db import models
from uuid import uuid4

class Customers(models.Model):
    id_customer = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    age = models.IntegerField()
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)