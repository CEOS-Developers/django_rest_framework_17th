from django.db import models

# Create your models here.

class Comment(models.Model) :
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

