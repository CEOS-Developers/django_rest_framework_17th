from django.urls import path, include
from community import views
from rest_framework.routers import DefaultRouter
from .views import *

# urlpatterns = [
#     path('boards/', views.BoardList.as_view()),
#     path('boards/<int:board_id>/', views.PostList.as_view()),
#     path('posts/<int:post_id>/', views.PostDetail.as_view()),
# ]


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('boards', BoardViewSet)

urlpatterns = [
    path('', include(router.urls))
]
