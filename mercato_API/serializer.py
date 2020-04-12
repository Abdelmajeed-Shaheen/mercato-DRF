from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers



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
