from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CustomerRegisterSerialiser(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    full_name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    birthday = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True,required=True)
    confirm_password = serializers.CharField(write_only=True,required=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password not match.")
        return data

    def create_user(self,validate_data):
        user = User.objects.create_user(
            email = validate_data['email'],
            full_name = validate_data['full_name'],
            address = validate_data['address'],
            phone = validate_data['phone'],
            birthday = validate_data['birthday'],

        )
        user.set_password(validate_data['password'])
        user.is_customer = True
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email',None)
        instance.full_name = validated_data.get('full_name',None)
        instance.address = validated_data.get('address',None)
        instance.phone = validated_data.get('phone',None)
        instance.birthday = validated_data.get('birthday',None)
        instance.save()

        password = validated_data.get('password',None)
        confirm_password = validated_data.get('confirm_password',None)
        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
        update_session_auth_hash(self.context.get('request'),instance)
        return instance

    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'confirm_password',
            'email',
            'full_name',
            'address',
            'phone',
            'birthday',
            'is_customer'
        )

class EmployeeRegisterSerialiser(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    full_name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    birthday = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password not match.")
        return data

    def create_user(self,validate_data):
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

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email',None)
        instance.full_name = validated_data.get('full_name',None)
        instance.address = validated_data.get('address',None)
        instance.phone = validated_data.get('phone',None)
        instance.birthday = validated_data.get('birthday',None)
        instance.save()

        password = validated_data.get('password',None)
        confirm_password = validated_data.get('confirm_password',None)
        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
        update_session_auth_hash(self.context.get('request'),instance)
        return instance

    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'confirm_password',
            'email',
            'full_name',
            'address',
            'phone',
            'birthday',
            'is_employee'
        )

class CustomerLoginSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User




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