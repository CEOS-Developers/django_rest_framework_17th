import datetime
from django.utils import timezone
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_time = models.DateTimeField('created time', auto_now_add=True)
    modified_time = models.DateTimeField('modified time', auto_now=True)

    class Meta:
        abstract = True  # Set this model as Abstract


class University(BaseModel):
    university_id = models.AutoField('primary key', primary_key=True)
    univ_name = models.CharField(max_length=100)

    def __str__(self):
        return self.univ_name


class Department(BaseModel):
    department_id = models.AutoField('primary key', primary_key=True)
    dept_name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.dept_name} : {self.university.univ_name}'
