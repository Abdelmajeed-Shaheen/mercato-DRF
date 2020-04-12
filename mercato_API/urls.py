from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import  RegisterAPI




urlpatterns = [

    path('api/register', RegisterAPI.as_view(), name='api-register'),
    path('api/login', TokenObtainPairView.as_view(), name='api-login'),

]
