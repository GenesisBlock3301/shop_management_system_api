from django.urls import path
from .views import *

urlpatterns = [
    path('reg/customer/', CustomerRegistrationView.as_view()),
    path('reg/employee/', EmployeeRegistrationView.as_view()),
    path('products/', ProductViewSet.as_view()),
    path('products/<pk>/', ProductDetailViewSet.as_view()),
    path('rating/', RatingViewSet.as_view()),
    path('comments/', CommentViewSet.as_view()),
    path('transactions/', TransactionViewSet.as_view()),
]
