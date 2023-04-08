from django.db import models

from accounts.models import User
from bases.models import BaseTimeModel


# Create your models here.


class Timetable(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timetables')
    name = models.CharField(max_length=10)
    courses = models.ManyToManyField('CourseDetail', null=True)

    def __str__(self):
        return '{}님의 시간표:{}'.format(self.user.nickname, self.name)


class Course(BaseTimeModel):
    title = models.CharField(max_length=20)
    professor = models.CharField(max_length=20)
    credit = models.IntegerField()
    hours = models.IntegerField()

    def __str__(self):
        return '{}-{}'.format(self.title, self.professor)


class CourseDetail(BaseTimeModel):

    DAY_CHOICES = [
        ('MON', '월'),
        ('TUE', '화'),
        ('WED', '수'),
        ('THU', '목'),
        ('FRI', '금'),
        ('SAT', '토'),
        ('SUN', '일')
    ]

    # 1~15교시 선택
    TIME_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15)
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_details')
    course_code = models.CharField(max_length=10)
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    time = models.IntegerField(choices=TIME_CHOICES)
    hours = models.IntegerField(default=1)
    classroom = models.CharField(max_length=10)

    def __str__(self):
        return self.course_code


class Friend(BaseTimeModel):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_list')
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return 'from user: {}, to user: {}'.format(self.from_user.username, self.to_user.username)

