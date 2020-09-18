from rest_framework import status,permissions
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from .models import *
from django.http import Http404
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model
from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import authenticate, login



class CustomerRegistrationView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerRegisterSerialiser


class EmployeeRegistrationView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmployeeRegisterSerialiser

class CustomerLoginView(APIView):
    model = get_user_model()
    def post(self,request,format=None):
        data = request.data
        # serializer = Cu
        email = data.get('email',None)
        passaword = data.get('password',None)
        user = authenticate(email=email,passaword=passaword)
        if user is not None:
            if user.is_active:
                login(request,user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProductViewSet(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self):
        serializer = ProductSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailViewSet(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, ):

        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class RatingViewSet(APIView):

    def get(self, request):
        rate = Rating.objects.all()
        serializer = RatingSerializer(rate, many=True)
        return Response(serializer.data)


class CommentViewSet(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class TransactionViewSet(APIView):

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)