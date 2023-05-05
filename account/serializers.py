from rest_framework import serializers
from account.models import *


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data.get('email')
        nickname = validated_data.get('nickname')
        school_id = validated_data.get('school_id')
        password = validated_data.get('password')
        user = MyUser(
            email=email,
            nickname=nickname,
            school_id=school_id
        )
        user.set_password(password)
        user.save()
        return user


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
