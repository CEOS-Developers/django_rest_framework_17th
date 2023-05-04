from django.urls import path, include
from rest_framework import routers
from .views import BoardViewSet

router = routers.DefaultRouter()
router.register(r'board', BoardViewSet)  # urls.py의 router

urlpatterns = router.urls
#
urlpatterns = [
    path('', include(router.urls)),
]
#
# app_name = 'board'
# urlpatterns = [
#     path('', views.AllBoardView.as_view(), name='all_board'),
#     path('<int:pk>/', views.OneBoardView.as_view(), name='index'),
#     # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     # path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
