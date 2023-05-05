from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status

class Login(APIView):

    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))

        if user is not None:
            token = TokenObtainPairSerializer.get_token(user)
            access_token = token.access_token
            res = Response(
                {
                    "message": "login success",
                    "token": str(token.access_token)
                },
                status=status.HTTP_200_OK,
            )

            res.set_cookie("access", access_token, httponly=True)
            return res
        else:
            return HttpResponse("target failed")
