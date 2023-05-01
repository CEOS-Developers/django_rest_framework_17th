from django.urls import path, include

from . import views

# router = routers.DefaultRouter()
# router.register('', TimetableViewSet)
# router.register('courses', CourseViewSet)
#
# urlpatterns = router.urls

urlpatterns = [
    path('', views.TimetableList.as_view()),
    path('<int:timetable_id>', views.TimetableDetail.as_view()),
    path('courses/', views.CourseDetailView.as_view()),
]