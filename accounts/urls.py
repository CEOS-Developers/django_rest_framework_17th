from django.urls import path
from accounts.views import home
from .views import register, login, logout
from . import views

urlpatterns = [
    path('', home),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view())
]