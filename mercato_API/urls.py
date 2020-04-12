from django.urls import path
from .views import ItemView

urlpatterns = [
    path('api/mercato/category/list/<int:category_id>', ItemView.as_view(), name='api-item-category-list'),
    path('api/mercato/subcategory/list/<int:category_id>/<int:sub_category_id>', ItemView.as_view(), name='api-item-subcategory-list'),
    path('api/mercato/item/detail/<int:item_id>', ItemView.as_view(), name='api-item-detail'),
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import  RegisterAPI




urlpatterns = [

    path('api/register', RegisterAPI.as_view(), name='api-register'),
    path('api/login', TokenObtainPairView.as_view(), name='api-login'),

