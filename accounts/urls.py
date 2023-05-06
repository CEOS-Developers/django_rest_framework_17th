from django.urls import path, include

from accounts.views import SignUp, SignIn, Logout

urlpatterns = [
    path("sign-up/", SignUp.as_view()),
    path("sign-in/", SignIn.as_view()),
    path("log-out/", Logout.as_view())
]