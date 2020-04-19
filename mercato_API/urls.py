from django.urls import path
from .views import ItemView,RegisterAPI, ListofCategoriesView,addOrder
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('items/', ItemView.as_view(), name='api-item-list'),
    path('items/<int:item_id>/', ItemView.as_view(), name='api-item-detail'),
    path('categories/<int:category_id>/', ItemView.as_view(), name='api-item-category-list'),
    path('subcategories/<int:sub_category_id>/', ItemView.as_view(), name='api-item-subcategory-list'),
    path('categories/', ListofCategoriesView.as_view(), name='api-category-list'),
    path('addorder/', addOrder, name='api-addorder'),
    path('register', RegisterAPI.as_view(), name='api-register'),
    path('login', TokenObtainPairView.as_view(), name='api-login'),
    ]
