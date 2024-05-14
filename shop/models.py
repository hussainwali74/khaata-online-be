from django.db import models
from django.utils import timezone

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self, *args, **kwargs):
        self.deleted_at = None
        self.save()

class Customer(TimestampedModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=355)
    contact_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='customers/', null=True, blank=True)

    def __str__(self):
        return self.name

class ItemCategory(TimestampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(TimestampedModel):
    detail = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='items/', null=True, blank=True)

    def __str__(self):
        return self.detail

class Bill(TimestampedModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='BillItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    received_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Bill {self.id} for {self.customer.name}'

class BillItem(TimestampedModel):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(TimestampedModel):
    name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    contact_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='employees/', null=True, blank=True)

    def __str__(self):
        return self.name

class Admin(TimestampedModel):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='admins/', null=True, blank=True)

    def __str__(self):
        return self.name
