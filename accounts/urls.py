from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from accounts.views import SignUp, SignIn, Logout

urlpatterns = [
    path("sign-up/", SignUp.as_view()),
    path("sign-in/", SignIn.as_view()),
    path("log-out/", Logout.as_view()),
    path("refresh/", TokenRefreshView.as_view())
]