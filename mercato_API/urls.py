from django.urls import path
from .views import ItemView, RegisterAPI, ListofCategoriesView, UserLoginAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


# URL naming is unconventional - let's have a talk about it
urlpatterns = [
    path('mercato/category/item/list/<int:category_id>',
         ItemView.as_view(), name='api-item-category-list'),
    path('mercato/subcategory/list/<int:category_id>/<int:sub_category_id>',
         ItemView.as_view(), name='api-item-subcategory-list'),
    path('mercato/item/detail/<int:item_id>',
         ItemView.as_view(), name='api-item-detail'),
    path('mercato/category/list/', ListofCategoriesView.as_view(),
         name='api-category-list'),
    path('register', RegisterAPI.as_view(), name='api-register'),
    path('login', UserLoginAPIView.as_view(), name='api-login'),
]
