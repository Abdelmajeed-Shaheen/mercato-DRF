from django.urls import path
from .views import ItemView, RegisterAPI, ListofCategoriesView, UserLoginAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


# URL naming is unconventional - let's have a talk about it
urlpatterns = [
    path('items/', ItemView.as_view(), name="api-item-list"),
    path('items/<int:item_id>/',
         ItemView.as_view(), name='api-item-detail'),
    path('categories/', ListofCategoriesView.as_view(),
         name='api-category-list'),
    path('categories/<int:category_id>/',
         ItemView.as_view(), name='api-item-category-list'),
    path('subcategories/<int:sub_category_id>/',
         ItemView.as_view(), name='api-item-subcategory-list'),
    path('register', RegisterAPI.as_view(), name='api-register'),
    path('login', UserLoginAPIView.as_view(), name='api-login'),
]
