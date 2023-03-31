from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(School)
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(CommentLike)
admin.site.register(CommentReplyLike)
admin.site.register(PostLike)
admin.site.register(Timetable)
admin.site.register(Course)
admin.site.register(CourseDetail)
admin.site.register(Friend)
admin.site.register(Scrap)



