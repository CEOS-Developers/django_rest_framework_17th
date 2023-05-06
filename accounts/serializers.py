from rest_framework import serializers
from accounts.models import *


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'nickname', 'name', 'school']

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        nickname = validated_data.get('nickname')
        name = validated_data.get('name')
        school = validated_data.get('school')

        user = User(
            username=username,
            email=email,
            nickname=nickname,
            name=name,
            school=school
        )
        user.set_password(password)
        user.save()
        return user

