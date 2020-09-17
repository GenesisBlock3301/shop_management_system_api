from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CustomerRegisterSerialiser(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self,validate_data):
        user = User.objects.create_user(
            email = validate_data['email'],
            password= validate_data['password'],
            full_name = validate_data['full_name'],
            address = validate_data['address'],
            phone = validate_data['phone'],
            birthday = validate_data['birthday'],

        )
        user.set_password(validate_data['password'])
        user.is_customer = True
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'email',
            'full_name',
            'address',
            'phone',
            'birthday',
            'is_customer'
        )

class EmployeeRegisterSerialiser(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self,validate_data):
        user = User.objects.create(
            email = validate_data['email'],
            # password= validate_data['password'],
            full_name = validate_data['full_name'],
            address = validate_data['address'],
            phone = validate_data['phone'],
            birthday = validate_data['birthday'],

        )
        user.set_password(validate_data['password'])
        user.is_employee = True
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'email',
            'full_name',
            'address',
            'phone',
            'birthday',
            'is_employee'
        )
        read_only_fields = ('id',)




class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['customer','product_name','product_type','stock','price','description','image']


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['product','customer','rate']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['user','product','message']


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['customer']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['customer']

class CartItem(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart','product','quantity','created_at','updated_at','active']