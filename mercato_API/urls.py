from django.urls import path
from .views import ItemView,RegisterAPI, ListofCategoriesView,addOrder,OrderHistory,UserDetail
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('items/', ItemView.as_view(), name='api-item-list'),
    path('items/<int:item_id>/', ItemView.as_view(), name='api-item-detail'),
    path('categories/<int:category_id>/', ItemView.as_view(), name='api-item-category-list'),
    path('subcategories/<int:sub_category_id>/', ItemView.as_view(), name='api-item-subcategory-list'),
    path('categories/', ListofCategoriesView.as_view(), name='api-category-list'),
    path('addorder/', addOrder, name='api-addorder'),
    path('orders/', OrderHistory.as_view(), name='api-orders'),
    path('user/', UserDetail.as_view(), name='api-user'),
    path('register', RegisterAPI.as_view(), name='api-register'),
    path('login', TokenObtainPairView.as_view(), name='api-login'),
    ]
