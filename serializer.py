from rest_framework import serializers
from django.contrib.auth.models import User
from .models import product, category, order_items, order, delievery

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only = True)
    _id = serializers.SerializerMethodField(read_only = True)
    isAdmin = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = 'User'
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self,obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.id
    
    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'

class DelieverySerializer(serializers.ModelSerializer):
    class Meta:
        model = delievery
        fields = '_all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_items
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only = True)
    delieveryAddress = serializers.SerializerMethodField(read_only = True)
    user = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = order
        fields = '__all__'

    def get_orderItems(self, obj):
        items = obj.order_items_set.all()
        serializer = OrderItemsSerializer(items, many=True)
        return serializer.data
    
    def get_delieveryAddress(self, obj):
        try:
            address = DelieverySerializer(
                obj.delieveryAddress, many = False).data
        except:
            address = False
        return address
    
    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many = False)
        return serializer.data