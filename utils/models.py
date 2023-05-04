from django.db import models


class BaseModel(models.Model):
    status = models.CharField(max_length=10, default='A')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
