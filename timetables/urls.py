from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('timetables', TimetableViewSet)
router.register('courses', CourseViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', include(urlpatterns)),
    # path('<int:timetable_id>', views.TimetableDetail.as_view()),
    # path('courses/', views.CourseDetailView.as_view()),
]