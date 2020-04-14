from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Category, Subcategory
from .serializer import ItemDetailSerializer,UserSerializer,CategoriesListSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import CreateAPIView

class RegisterAPI(CreateAPIView):
	serializer_class = UserSerializer

class ItemView (APIView):
	def get(self, request, item_id = None, category_id = None, sub_category_id = None):
		items = Item.objects.all()
		if (item_id):
			itemobj = items.get(id = item_id)
			serializer = ItemDetailSerializer(itemobj)
			return Response(serializer.data)
		if (category_id):
			category = Category.objects.get (id = category_id)
			items = items.filter(category=category)
		elif (sub_category_id):
			sub_category = Subcategory.objects.get (id = sub_category_id)
			items = items.filter(sub_category=sub_category)
		serializer = ItemDetailSerializer(items, many=True)
		return Response(serializer.data)

class ListofCategoriesView(APIView):
	def get(self, request):
		categories_list = Category.objects.all()
		serializer=CategoriesListSerializer(categories_list, many=True)
		return Response(serializer.data)
