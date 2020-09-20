from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from rest_framework import exceptions




class UserSerializer(serializers.ModelSerializer):
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
        )


class CustomerRegisterSerialiser(serializers.ModelSerializer):
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

    # def create_user(self, validate_data):
        # user = User.objects.create_user(
        #     email=validate_data['email'],
        #     full_name=validate_data['full_name'],
        #     address=validate_data['address'],
        #     phone=validate_data['phone'],
        #     birthday=validate_data['birthday'],
        #
        # )
        # user.set_password(validate_data['password'])
        # user.is_customer = True
        # user.save()
        # return user
    def create(self, validated_data):
        """creates user with encrypted password and retruns the user"""
        return get_user_model().objects.create_user(**validated_data)


    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', None)
        instance.full_name = validated_data.get('full_name', None)
        instance.address = validated_data.get('address', None)
        instance.phone = validated_data.get('phone', None)
        instance.birthday = validated_data.get('birthday', None)
        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)
        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
        update_session_auth_hash(self.context.get('request'), instance)
        return instance

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'confirm_password',
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

    def create_user(self, validate_data):
        user = User.objects.create(
            email=validate_data['email'],
            # password= validate_data['password'],
            full_name=validate_data['full_name'],
            address=validate_data['address'],
            phone=validate_data['phone'],
            birthday=validate_data['birthday'],

        )
        user.set_password(validate_data['password'])
        user.is_employee = True
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', None)
        instance.full_name = validated_data.get('full_name', None)
        instance.address = validated_data.get('address', None)
        instance.phone = validated_data.get('phone', None)
        instance.birthday = validated_data.get('birthday', None)
        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)
        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
        update_session_auth_hash(self.context.get('request'), instance)
        return instance

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'confirm_password',
            'full_name',
            'address',
            'phone',
            'birthday',
            'is_employee'
        )


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email and password:
            user = authenticate(email=email,password=password)
            print("--------------------------------------------",user)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data
    class Meta:
        model = User
        fields = (
            'email',
            'password',

        )

# class EmployeeLoginSerializer(serializers.Serializer):
#     email = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)
#
#     def validate(self, data):
#         email = data.get("email", "")
#         password = data.get("password", "")
#
#         if email and password:
#             user = authenticate(email=email, password=password)
#             if user:
#                 if user.is_active:
#                     data["user"] = user
#                 else:
#                     msg = "User is deactivated."
#                     raise exceptions.ValidationError(msg)
#             else:
#                 msg = "Unable to login with given credentials."
#                 raise exceptions.ValidationError(msg)
#         else:
#             msg = "Must provide username and password both."
#             raise exceptions.ValidationError(msg)
#         return data



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['customer', 'product_name', 'product_type', 'stock', 'price', 'description', 'image']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['product', 'customer', 'rate']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'product', 'message']


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
        fields = ['cart', 'product', 'quantity', 'created_at', 'updated_at', 'active']
