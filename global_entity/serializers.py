from rest_framework import serializers
from .models import *

class UniversitySerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    # TODO university 외래키로 추가함

    class Meta:
        model = University  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함

class DepartmentSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    # TODO university 외래키로 추가함

    class Meta:
        model = Department  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함
