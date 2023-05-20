from django.urls import path, include
from account import views


urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("logout/", views.LogoutAPIView.as_view()),
    path("token-refresh/", views.RefreshAccessToken.as_view()),
    path("health-check/", views.HealthCheck.as_view()),
]
