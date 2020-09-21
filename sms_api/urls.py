
from django.contrib import admin
from django.urls import path,include
from shopApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('shopApp.urls')),
    # path('api/auth/',include('djoser.urls.authtoken'))
    path('reg/customer/', CustomerRegistrationView.as_view()),
    path('reg/employee/', EmployeeRegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LoginView.as_view()),
]
