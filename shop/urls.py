from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ItemViewSet, BillViewSet, RoleViewSet, EmployeeViewSet, AdminViewSet, ItemCategoryViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'items', ItemViewSet)
router.register(r'bills', BillViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'item-categories', ItemCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
