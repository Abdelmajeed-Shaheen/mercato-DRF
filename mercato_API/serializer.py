from rest_framework import serializers
from .models import Item, Category, Subcategory
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings


# Unnecessary
# Don't re-invent the wheel - especially when it comes to cybersecurity
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')
        try:
            user_obj = User.objects.get(username=my_username)
        except:
            raise serializers.ValidationError("This username does not exist")
        if not user_obj.check_password(my_password):
            raise serializers.ValidationError(
                "Incorrect username/password combination!")
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        data["token"] = token
        return data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'token']

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username,
                        first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()

        #############
        # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/creating_tokens_manually.html
        #############
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)

        validated_data['token'] = token
        return validated_data


class CategoriesListSerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'subcategories']

    def get_subcategories(self, categoryobj):
        result = []
        for subcategory in Subcategory.objects.filter(category=categoryobj):
            result.append(subcategory.name)
        return result


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name']


class ItemDetailSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer()
    sub_category = SubCategoriesSerializer()

    class Meta:
        model = Item
        fields = '__all__'
