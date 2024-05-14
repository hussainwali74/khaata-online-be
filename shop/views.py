from rest_framework import viewsets
from .models import Customer, Item, Bill, Role, Employee, Admin, ItemCategory
from .serializers import CustomerSerializer, ItemSerializer, BillSerializer, RoleSerializer, EmployeeSerializer, AdminSerializer, ItemCategorySerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.filter(deleted_at__isnull=True)
    serializer_class = CustomerSerializer

class ItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = ItemCategory.objects.filter(deleted_at__isnull=True)
    serializer_class = ItemCategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(deleted_at__isnull=True)
    serializer_class = ItemSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.filter(deleted_at__isnull=True)
    serializer_class = BillSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(deleted_at__isnull=True)
    serializer_class = EmployeeSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.filter(deleted_at__isnull=True)
    serializer_class = AdminSerializer
