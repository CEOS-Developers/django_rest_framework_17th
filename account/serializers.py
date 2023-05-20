from rest_framework import serializers
from account.models import *


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    school = SchoolSerializer

    class Meta:
        model = MyUser
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data.get('email')
        nickname = validated_data.get('nickname')
        school = validated_data.get('school')
        password = validated_data.get('password')
        user = MyUser(
            email=email,
            nickname=nickname,
            school=school
        )
        user.set_password(password)
        user.save()
        return user


# class ProfileSerializer(serializers.ModelSerializer):
#     school = SchoolSerializer(read_only=True)
#
#     class Meta:
#         model = Profile
#         fields = '__all__'
