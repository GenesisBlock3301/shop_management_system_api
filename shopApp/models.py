from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin


class CustomUserManager(BaseUserManager):
    """custom user email where email is unique.
    We can also pass Full name , email and password here"""

    def create_user(self,email,password,**extra_fields):
        """Create and save a User given email and password"""
        if not email:
            raise ValueError(_("The Email is must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        """Create and save Super user with given email address"""
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Supperuser must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Supperuser must have is_superuser=True"))

        return self.create_user(email,password,**extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.EmailField(_('email_address'),unique=True)

    full_name = models.CharField(max_length=150,default='Unknown')
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    birthday = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

"""
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email_address'),unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='employees')
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    birthday = models.CharField(max_length=150)

    def __str__(self):
        return f"Employee name is {self.user.username}"

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customers')
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    birthday = models.CharField(max_length=150)

    def __str__(self):
        return f"Customer name is {self.full_name}"
"""

class Product(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='customers')
    product_name = models.CharField(max_length=150)
    product_type = models.CharField(max_length=150)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=100,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return  self.product_name


class Rating(models.Model):
    # one to many field
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

    def __str__(self):
        return f"Product name {self.product} and ratine is {self.rate}"

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"In {self.product.product_name} commented by {self.user.email}"

class Transaction(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approval_status = models.BooleanField(default=False)

    def total_cost(self):
        return self.quantity*self.product.price


    def __str__(self):
        return self.product.product_name



class Cart(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart# {self.customer}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='carts')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Oreder# {self.id} of {self.product.product_name}"




