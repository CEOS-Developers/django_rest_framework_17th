from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('boards', BoardViewSet, basename=Board)   # register()함으로써 두 개의 url 생성
router.register('posts', PostViewSet, basename=Post)


urlpatterns = router.urls

urlpatterns = [
    path('', include(urlpatterns)),
    # path('<int:board_id>/', views.PostList.as_view()),
    # path('<int:board_id>/<int:post_id>/', views.PostDetail.as_view()),
]
