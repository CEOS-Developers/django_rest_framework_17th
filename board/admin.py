from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LikePost)
admin.site.register(ScrapPost)
admin.site.register(BlackPost)
admin.site.register(LikeComment)
admin.site.register(BlackComment)
