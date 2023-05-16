from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RefreshToken(RefreshToken):
    def for_user(cls, user):
        token = super().for_user(user)
        return token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        login_id = validated_data.get('login_id')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User(
            login_id=login_id,
            email=email
        )
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
 id = serializers.CharField(write_only=True, required=True)
 password = serializers.CharField(write_only=True, required=True)

 def validate(self, request, username=None):
     id = request.get('id', None)
     password = request.get('password', None)

     if User.objects.filter(username=id).exists():
         user = User.objects.get(username=id)

         if user.password != password:
             raise serializers.ValidationError({"Wrong Password"})
         # if not user.check_password(password):
         #     raise serializers.ValidationError({"Wrong Password"})
     else:
         raise serializers.ValidationError({"User doesn't exist."})

     token = RefreshToken().for_user(user)
     refresh = str(token)
     access = str(token.access_token)

     data = {
         'id': user.id,
         'refresh': refresh,
         'access': access
     }

     return data

