from rest_framework import serializers
from .models import User, Product, Admin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('ism', 'phone')

class AddProductSRL(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class AdminSRL(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"











