from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import SignUp, SignIn, SignOut

urlpatterns = [
    path("sign-up/", SignUp.as_view()),
    path("sign-in/", SignIn.as_view()),
    path("sign-out/", SignOut.as_view()),
    path("refresh/", TokenRefreshView.as_view())
]
