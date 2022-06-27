from attr import fields
from rest_framework import serializers
from .models import OrderCustomer, Product, ProfileVendor,OrderIteamCustomer
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderCustomer    
        fields='__all__' 

class OrderIteamCustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderIteamCustomer 
        fields='__all__'      

class ProductIdActtionSerializer(serializers.ModelSerializer):
    action = serializers.CharField(max_length=20)
    class Meta:
        model = OrderIteamCustomer
        fields =['product','action']


class CheckOutProductAddSerializer(serializers.ModelSerializer):
    button = serializers.CharField(max_length=100)
    class Meta:
        model = OrderIteamCustomer
        fields =['id','button']