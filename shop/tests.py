from django.test import TestCase
from .models import Customer, Item, Bill, BillItem, Role, Employee, Admin, ItemCategory

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="John Doe", address="123 Main St", contact_number="555-555-5555")

    def test_customer_creation(self):
        customer = Customer.objects.get(name="John Doe")
        self.assertEqual(customer.name, "John Doe")

class ItemTestCase(TestCase):
    def setUp(self):
        category = ItemCategory.objects.create(name="Electronics")
        Item.objects.create(detail="Laptop", rate=1000.00, category=category, size="Medium")

    def test_item_creation(self):
        item = Item.objects.get(detail="Laptop")
        self.assertEqual(item.detail, "Laptop")
        self.assertEqual(item.category.name, "Electronics")

class BillTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="Jane Doe", address="456 Main St", contact_number="555-555-5556")
        category = ItemCategory.objects.create(name="Appliances")
        item = Item.objects.create(detail="Washing Machine", rate=500.00, category=category, size="Large")
        bill = Bill.objects.create(customer=customer, total_amount=500.00, discount=50.00, received_amount=450.00, remaining_amount=50.00)
        BillItem.objects.create(bill=bill, item=item, quantity=1, price=450.00)

    def test_bill_creation(self):
        bill = Bill.objects.get(customer__name="Jane Doe")
        self.assertEqual(bill.total_amount, 500.00)
        self.assertEqual(bill.discount, 50.00)
        self.assertEqual(bill.received_amount, 450.00)
        self.assertEqual(bill.remaining_amount, 50.00)
