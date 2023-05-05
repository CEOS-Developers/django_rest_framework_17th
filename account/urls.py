from django.db import router
from django.urls import include, path

from account.views import RegisterAPIView, AuthView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), #회원가입하기
    path("auth/", AuthView.as_view()), #로그인하기
]