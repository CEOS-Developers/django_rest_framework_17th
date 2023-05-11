from django.db import router
from django.urls import include, path

from account.views import RegisterAPIView, AuthView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), #회원가입하기
    path("auth/", AuthView.as_view()), #로그인하기
    path('auth/refresh/', TokenRefreshView.as_view()),#토큰 재발급하기
]