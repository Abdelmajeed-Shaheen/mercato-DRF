from rest_framework import serializers
from .models import Item, Category, Subcategory
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name','token']

	def create(self, validated_data):
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username,first_name=first_name,last_name=last_name)
		new_user.set_password(password)
		new_user.save()
		user = User.objects.get(username=username)
		return get_tokens_for_user(user)



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
