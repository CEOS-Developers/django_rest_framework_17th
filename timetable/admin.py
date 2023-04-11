from django.contrib import admin

from timetable.models import *

admin.site.register(TimeTable)
admin.site.register(LectureDomain)
admin.site.register(Lecture)
admin.site.register(TakeLecture)
admin.site.register(LectureReview)
admin.site.register(ReviewLike)
