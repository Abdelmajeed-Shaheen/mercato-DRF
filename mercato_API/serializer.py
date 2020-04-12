from rest_framework import serializers
from .models import Item, Category, Subcategory
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only = True)

	class Meta:
		model = User
		fields = ['first_name','last_name','username','password']

	def create(self,validated_data):
		username = validated_data.get('username')
		password = validated_data.get('password')
		first_name = validated_data.get('first_name')
		last_name = validated_data.get('last_name')

		user = User(username = username,first_name = first_name , last_name = last_name)
		user.set_password(password)
		user.save()
		return validated_data



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
