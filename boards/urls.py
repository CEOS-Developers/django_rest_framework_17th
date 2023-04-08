from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardList.as_view()),
    path('<int:board_id>/', views.PostList.as_view()),
    path('<int:board_id>/<int:post_id>/', view.PostDetail.as_view()),
]
