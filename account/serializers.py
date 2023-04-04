from rest_framework import serializers
from .models import *
from global_entity.serializers import *


class UserSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    university = UniversitySerializer()
    class Meta:
        model = User  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함
