import jwt
from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from django.contrib.auth import authenticate
from django_rest_framework_17th.settings.base import SECRET_KEY


# 회원 가입
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 로그인
class LoginAPIView(APIView):
    def post(self, request):
        # 유저 인증
        myUser = authenticate(
            email=request.data.get("email"), password=request.data.get("password")
        )
        # 해당 이메일, 비밀 번호로 가입한 유저가 있는 경우
        if myUser is not None:
            serializer = MyUserSerializer(myUser)
            # jwt, refresh token 발급
            token = TokenObtainPairSerializer.get_token(myUser)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "Login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            # refresh token 은 쿠키에 저장
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        else:
            print("Login error")
            return Response(
                {"message": "Failed to login"},
                status=status.HTTP_400_BAD_REQUEST
            )


class RefreshAccessToken(APIView):
    def post(self, request):
        # 쿠키에 저장된 refresh 토큰 확인
        refresh_token = request.COOKIES.get('refresh')

        if refresh_token is None:
            return Response({
                "message": "Refresh token does not exist"
            }, status=status.HTTP_403_FORBIDDEN)

        # refresh 토큰 디코딩 진행
        try:
            payload = jwt.decode(
                refresh_token, SECRET_KEY, algorithms=['HS256']
            )
        except:
            # refresh 토큰도 만료된 경우 에러 처리
            return Response({
                "message": "Expired refresh token, please login again"
            }, status=status.HTTP_403_FORBIDDEN)

        # 해당 refresh 토큰을 가진 유저 정보 불러 오기
        user = MyUser.objects.get(id=payload['user_id'])

        if user is None:
            return Response({
                "message": "User not found"
            }, status=status.HTTP_400_BAD_REQUEST)
        if not user.is_active:
            return Response({
                "message": "User is inactive"
            }, status=status.HTTP_400_BAD_REQUEST)

        # access 토큰 재발급 (유효한 refresh 토큰을 가진 경우에만)
        token = TokenObtainPairSerializer.get_token(user)
        access_token = str(token.access_token)

        return Response(
            {
                "message": "New access token",
                "access_token": access_token
            },
            status=status.HTTP_200_OK
        )


# 로그 아웃
class LogoutAPIView(APIView):
    def post(self, request):
        # 클라이언트의 쿠키에 저장된 refresh 토큰을 삭제함으로써 로그 아웃 처리
        response = Response({
            "message": "Logout success"
        }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie('refresh')
        return response


class HealthCheck(APIView):
    def get(self, request, format=None):
        response = Response({
            "message": "Instance is healthy!"
        }, status=status.HTTP_200_OK)
        return response
