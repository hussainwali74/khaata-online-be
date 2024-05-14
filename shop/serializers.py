from rest_framework import serializers
from .models import Customer, Item, Bill, BillItem, Role, Employee, Admin, ItemCategory


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class BillItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillItem
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    items = BillItemSerializer(many=True)

    class Meta:
        model = Bill
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        bill = Bill.objects.create(**validated_data)
        for item_data in items_data:
            BillItem.objects.create(bill=bill, **item_data)
        return bill

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.customer = validated_data.get('customer', instance.customer)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.received_amount = validated_data.get('received_amount', instance.received_amount)
        instance.remaining_amount = validated_data.get('remaining_amount', instance.remaining_amount)
        instance.save()

        instance.items.clear()
        for item_data in items_data:
            BillItem.objects.create(bill=instance, **item_data)
        return instance


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
