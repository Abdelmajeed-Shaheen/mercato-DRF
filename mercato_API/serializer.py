from rest_framework import serializers
from .models import Item, Category, Subcategory , OrderItem, Order
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

# this isn't being used anywhere
def get_tokens_for_user(user):
	refresh = RefreshToken.for_user(user)

	return {
		'refresh': str(refresh),
		'access': str(refresh.access_token),
	}

class UserSerializer(serializers.ModelSerializer):
	tokens = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = ('username', 'password', 'first_name','last_name', 'tokens')
		extra_kwargs = {'password': {'write_only': True}}

	def get_tokens(self, user):
		tokens = RefreshToken.for_user(user)
		refresh = str(tokens)
		access = str(tokens.access_token)
		data = {
			"refresh": refresh,
			"access": access
		}
		return data

	def create(self, validated_data):
		user =User(
			username=validated_data['username'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
		)
		user.set_password(validated_data['password'])
		user.save()
		return user



class CategoriesListSerializer(serializers.ModelSerializer):
	subcategories = serializers.SerializerMethodField()
	class Meta:
		model = Category
		fields= ['id', 'name', 'image', 'subcategories']
	def get_subcategories(self, categoryobj):
		result = []
		for subcategory in Subcategory.objects.filter(category = categoryobj):
			result.append(subcategory.name)
		return result


class CategoriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields= ['name']

class SubCategoriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subcategory
		fields= ['name']

class ItemDetailSerializer(serializers.ModelSerializer):
	category = CategoriesSerializer()
	sub_category = SubCategoriesSerializer()
	class Meta:
		model = Item
		fields= '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields= '__all__'

class OrderSerializer(serializers.ModelSerializer):
	products=serializers.StringRelatedField(many=True)
	class Meta:
		model=Order
		fields='__all__'

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name','last_name','email','date_joined']
