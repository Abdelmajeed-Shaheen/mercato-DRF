from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Category, Subcategory
from .serializer import ItemDetailSerializer, UserSerializer, CategoriesListSerializer, UserLoginSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import CreateAPIView


# Why do you have this?
# You should use the TokenObtainPairView
class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class RegisterAPI(CreateAPIView):
    serializer_class = UserSerializer


class ItemView (APIView):
    '''
    Needs to be refactored - let's have a talk about it
    '''

    def get(self, request, item_id=None, category_id=None, sub_category_id=None):
        if (item_id):
            itemobj = Item.objects.get(id=item_id)
            serializer = ItemDetailSerializer(itemobj)
            return Response(serializer.data)

        if (category_id and not sub_category_id):
            category = Category.objects.get(id=category_id)
            itemslist = Item.objects.filter(category=category)
            serializer = ItemDetailSerializer(itemslist, many=True)
            return Response(serializer.data)

        if (category_id and sub_category_id):
            sub_category = Subcategory.objects.get(id=sub_category_id)
            itemslist = Item.objects.filter(sub_category=sub_category)
            serializer = ItemDetailSerializer(itemslist, many=True)
            return Response(serializer.data)


class ListofCategoriesView(APIView):
    def get(self, request):
        categories_list = Category.objects.all()
        serializer = CategoriesListSerializer(categories_list, many=True)
        return Response(serializer.data)
