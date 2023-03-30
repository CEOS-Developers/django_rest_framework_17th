import datetime
from django.utils import timezone
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_time = models.DateTimeField('created time', auto_now_add=True)
    modified_time = models.DateTimeField('modified time', auto_now=True)


class University(BaseModel):
    univ_name = models.CharField(max_length=100)


class Department(BaseModel):
    dept_name = models.CharField(max_length=100)
    univ = models.ForeignKey(University, on_delete=models.PROTECT)
