from django.db import models
from utils.models import BaseModel
from account.models import *


class TimeTable(BaseModel):
    profile = models.ForeignKey("account.Profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    lecture = models.ManyToManyField("Lecture", through="TakeLecture")

    def __str__(self):
        return self.name


class LectureDomain(BaseModel):
    name = models.CharField(max_length=60)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name


class Lecture(BaseModel):
    name = models.CharField(max_length=150)
    lectureDomain = models.ForeignKey("LectureDomain", on_delete=models.CASCADE, blank=True)
    collegeYear = models.CharField(max_length=10, default='0')
    credit = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    lectureCode = models.CharField(max_length=60)
    classRoom = models.CharField(max_length=100)
    dayAndTime = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TakeLecture(BaseModel):
    timeTable = models.ForeignKey("TimeTable", on_delete=models.CASCADE, default='')
    lecture = models.ForeignKey("Lecture", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} started taking {self.lecture}"


class LectureReview(BaseModel):
    lecture = models.ForeignKey("Lecture", on_delete=models.CASCADE)
    profile = models.ForeignKey("account.Profile", on_delete=models.CASCADE)
    rating = models.CharField(max_length=10)
    contents = models.CharField(max_length=200)

    def __str__(self):
        return self.contents


class ReviewLike(BaseModel):
    lectureReview = models.ForeignKey("LectureReview", on_delete=models.CASCADE)
    profile = models.ForeignKey("account.Profile", related_name="profiles", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} 's like on {self.lectureReview}"
