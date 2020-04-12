from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Category, Subcategory
from .serializer import ItemDetailSerializer,UserSerializer
from rest_framework.generics import CreateAPIView


class ItemView (APIView):
    def get(self, request, item_id = None, category_id = None, sub_category_id = None):
        if (item_id):
            itemobj = Item.objects.get(id = item_id)
            serializer = ItemDetailSerializer(itemobj)
            return Response(serializer.data)

        if (category_id and not sub_category_id):
            category = Category.objects.get (id = category_id)
            itemslist = Item.objects.filter(category=category)
            serializer = ItemDetailSerializer(itemslist, many=True)
            return Response(serializer.data)

        if (category_id and sub_category_id):
            sub_category = Subcategory.objects.get (id = sub_category_id)
            itemslist = Item.objects.filter(sub_category=sub_category)
            serializer = ItemDetailSerializer(itemslist, many=True)
            return Response(serializer.data)


class RegisterAPI(CreateAPIView):
    serializer_class = UserSerializer
