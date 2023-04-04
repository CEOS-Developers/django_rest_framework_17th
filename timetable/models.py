from django.db import models
from global_entity.models import BaseModel, Department
from account.models import User


# Create your models here.

class Subject(BaseModel):
    subject_id = models.AutoField('primary key', primary_key=True)

    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    subject_name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=200)
    subject_grade = models.IntegerField()

    def __str__(self):
        return f'{self.department.university.univ_name} {self.department.dept_name} {self.subject_name} {self.subject_code}'


class Lecture(BaseModel):
    lecture_id = models.AutoField('primary key', primary_key=True)

    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    listener = models.ForeignKey(User, on_delete=models.PROTECT)

    semester = models.CharField(max_length=200)
    classroom = models.CharField(max_length=200)
    professor_name = models.CharField(max_length=200)
    lecture_time = models.CharField(max_length=200)

    score = models.FloatField()

    def __str__(self):
        return f'{self.subject.subject_name} {self.classroom} {self.semester} {self.listener.nickname}'
