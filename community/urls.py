from django.urls import path
from community import views

urlpatterns = [
    path('boards/', views.BoardList.as_view()),
    path('boards/<int:board_id>/', views.PostList.as_view()),
    path('posts/<int:post_id>/', views.PostDetail.as_view()),
]