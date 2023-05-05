from django.urls import path, include
from rest_framework import routers
from .views import BoardViewSet

app_name = 'board'
router = routers.DefaultRouter()
router.register('board', BoardViewSet)  # urls.py의 router

#
urlpatterns = [
    path('', include(router.urls)),
]
#
# urlpatterns = [
#     path('', views.AllBoardView.as_view(), name='all_board'),
#     path('<int:pk>/', views.OneBoardView.as_view(), name='index'),
#     # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     # path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
