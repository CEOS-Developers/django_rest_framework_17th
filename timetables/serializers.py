from rest_framework import serializers
from timetables.models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['created_at', 'modified_at']


class CourseDetailSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = CourseDetail
        exclude = ['created_at', 'modified_at', 'course']


class TimetableSerializer(serializers.ModelSerializer):
    courses = CourseDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Timetable
        fields = ['user', 'name', 'courses', 'is_default']


class TimetableListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ['id', 'user', 'name', 'is_default']


class FriendSerializer(serializers.ModelSerializer):
    friend_name = serializers.SerializerMethodField()

    class Meta:
        model = Friend
        fields = ['id', 'friend_name']

    def get_friend_name(self, obj):
        return obj.to_user.last_name + obj.to_user.first_name
