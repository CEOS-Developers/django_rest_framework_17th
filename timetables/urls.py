from django.urls import path
from . import views

urlpatterns = [
    path('', views.TimetableList.as_view()),
    path('<int:timetable_id>/', views.TimetableDetail.as_view()),
    path('courses/', views.CourseDetailView.as_view())
]