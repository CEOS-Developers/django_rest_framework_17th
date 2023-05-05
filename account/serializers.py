from rest_framework import serializers
from .models import *
from global_entity.serializers import *


class UserSerializer(serializers.ModelSerializer):
    university = UniversitySerializer
    class Meta:
        model = User  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함
