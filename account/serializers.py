from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        login_id = validated_data.get('login_id')
        password = validated_data.get('password')
        username = validated_data.get('username')
        univ = validated_data.get('univ')
        email = validated_data.get('email')
        profile_image = validated_data.get('profile_image')
        user = User(
            login_id=login_id,
            username=username,
            univ=univ,
            email=email,
            profile_image=profile_image
        )
        user.set_password(password)
        user.save()
        return user


class FriendListSerializer(serializers.ModelSerializer):
    user = UserSerializer
    friend = UserSerializer

    class Meta:
        model = FriendList
        field = ['user', 'friend']
