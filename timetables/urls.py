from django.urls import path
from .views import *


app_name = 'timetables'
urlpatterns = [
    # path('home/', home, name='home'),
    # path('detail/<int:timetable_id>', detail, name='detail'),
    # path('new/', new, name='new'),
    # path('create/', create, name='create'),
    #
    #
    # path('new_subject.html/<int:timetable_id>/', new_subject, name='new_subject'),
    # path('create_subject/<int:timetable_id>/', create_subject, name='create_subject'),

    path('', TimetableList.as_view()),
    path('<int:timetable_id>/', TimetableDetail.as_view()),
    # path('comment/', CommentList.as_view()),
    # path('comment/<int:comment_id>/', CommentDetail.as_view()),

]