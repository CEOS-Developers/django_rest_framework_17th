from django.contrib import admin

from api.models import *

admin.site.register(Profile)
admin.site.register(School)
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(PostLike)
admin.site.register(CommentLike)
admin.site.register(Scrap)
admin.site.register(TimeTable)
admin.site.register(LectureDomain)
admin.site.register(Lecture)
admin.site.register(TakeLecture)
admin.site.register(LectureReview)
admin.site.register(ReviewLike)