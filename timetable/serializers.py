from rest_framework import serializers
from .models import *
from global_entity.models import *


class SubjectSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    department = Department()

    class Meta:
        model = Subject  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함


class LectureSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    subject = Subject()
    listener = User()

    class Meta:
        model = Lecture  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함
