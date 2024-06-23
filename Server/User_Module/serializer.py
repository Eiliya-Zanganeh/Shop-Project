from User_Module.models import UserModel, CartModel
from rest_framework import serializers
from Product_Module.serializer import ProductSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = CartModel
        fields = '__all__'
