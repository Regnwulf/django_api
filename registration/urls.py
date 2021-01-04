from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from customers.api import viewsets as customersviewsets

route = routers.DefaultRouter()

route.register(r'customers', customersviewsets.CustomersViewSet, basename="Customers")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
