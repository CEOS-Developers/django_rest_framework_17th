from django.urls import path, include

from accounts.views import SignUp, SignIn

urlpatterns = [
    path("sign-up/", SignUp.as_view()),
    path("sign-in/", SignIn.as_view()),
]