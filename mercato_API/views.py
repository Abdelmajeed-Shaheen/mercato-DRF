from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Category, Subcategory,Order,OrderItem
from django.contrib.auth.models import User
from .serializer import ItemDetailSerializer,UserSerializer,CategoriesListSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import json


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


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def addOrder(request):
	if( not request.data):
		return Response({'cart':f'your cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
	received_json_data=json.loads(request.data)['cart']
	for cartitem in received_json_data:
		item=Item.objects.get(id=cartitem['item']['id'])
		if item.in_stock < cartitem['quantity']:
			return Response({'in_stock':f'requested quantity for {item.name} is not available'}, status=status.HTTP_400_BAD_REQUEST)
	user = request.user
	order=Order(user=user)
	order.save()
	for cartitem in received_json_data:
		item=Item.objects.get(id=cartitem['item']['id'])
		if item.in_stock < cartitem['quantity']:
			return Response({'in_stock':'requested quantity is not available'}, status=status.HTTP_400_BAD_REQUEST)
		item.in_stock=item.in_stock - cartitem['quantity']
		item.save()
		orderitem=OrderItem(order=order,item=item,quantity=cartitem['quantity'])
		orderitem.save()
	return Response({'created':'Your Order is placed'}, status=status.HTTP_200_OK)
