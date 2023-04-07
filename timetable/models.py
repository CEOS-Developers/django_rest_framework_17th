from django.db import models

from account.models import BaseModel, User


# Create your models here.

class CourseInfo(BaseModel):
    course_name = models.CharField(max_length=255)
    professor = models.CharField(max_length=255)

    class Meta:
        db_table = 'CourseInfo'
        unique_together = (('course_name', 'professor'),)

    def __str__(self):
        return '{} of {}'.format(self.course_name, self.professor)


# class Classroom(BaseModel):
#     class_field = models.CharField(max_length=255)
#
#
# class Time(BaseModel):
#     day = models.CharField(max_length=255)
#     period = models.CharField(max_length=255)


class Course(BaseModel):
    course_info = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    # classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # time = models.ForeignKey(Time, on_delete=models.CASCADE)
    year_semester = models.CharField(max_length=255)
    credits = models.IntegerField()
    course_number = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    classroom = models.CharField(max_length=255)

    def __str__(self):
        return '{} of {}'.format(self.course_info.course_name, self.course_number)


class Timetable(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return '{} take {}'.format(self.user.username, self.course.course_info.course_name)


class Review(BaseModel):
    course_info = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    score = models.IntegerField()
    content = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)

    def __str__(self):
        return self.content
