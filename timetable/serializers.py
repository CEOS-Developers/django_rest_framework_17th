from rest_framework import serializers
from account.serializers import UserSerializer
from .models import *


class CourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInfo
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    course_info = CourseInfoSerializer

    class Meta:
        model = Course
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):
    user = UserSerializer
    course = CourseSerializer

    class Meta:
        model = Timetable
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    course_info = CourseInfoSerializer

    class Meta:
        model = Review
        fields = '__all__'
