from rest_framework import serializers
from accounts.models import *


class SchoolSerializer(serializers.Serializer):
    class Meta:
        model = School
        fields = ['id', 'name']




