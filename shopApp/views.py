from rest_framework import status, permissions
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from .models import *
from django.http import Http404
from rest_framework.generics import CreateAPIView,GenericAPIView
from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout


class UserListView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    def get(self, request, format=None):
        user = [user.email for user in User.objects.all()]

        return Response(user, status=status.HTTP_200_OK)


class CustomerRegistrationView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerRegisterSerialiser


class EmployeeRegistrationView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmployeeRegisterSerialiser



class LoginView(APIView):
    serializer_class = LoginSerializer #field of rest api
    # permission_classes = [AllowAny=]
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']
        # django_login(request,user)
        # token, created = Token.objects.get_or_create(user=user)
        # return Response({"token": token.key}, status=status.HTTP_200_OK)
        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            user = authenticate(request,email=email,password=password)
            if user:
                django_login(request,user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)





# class EmployeeLoginView(GenericAPIView):
#     serializer_class = EmployeeLoginSerializer
#     # permission_classes = [AllowAny]
#     def post(self,request):
#         serializer = CustomerLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         django_login(request,user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key}, status=status.HTTP_200_OK)


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
