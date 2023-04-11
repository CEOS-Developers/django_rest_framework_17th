from django.contrib import admin

from community.models import *

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(PostLike)
admin.site.register(CommentLike)
admin.site.register(Scrap)
