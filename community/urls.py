from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import *

router = DefaultRouter()

router.register('post', PostViewSet)

app_name = 'community'
# urlpatterns = [
#     path('post/', views.PostList.as_view()),
#     path('post/<int:pk>/', views.PostDetail.as_view())
# ]

urlpatterns = router.urls
