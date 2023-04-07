from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FriendListSerializer(serializers.ModelSerializer):
    user = UserSerializer
    friend = UserSerializer

    class Meta:
        model = FriendList
        field = ['user', 'friend']
