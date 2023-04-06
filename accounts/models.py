from django.contrib.auth.models import User
from django.db import models

from bases.models import BaseTimeModel


# Create your models here.


class School(BaseTimeModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='users')
    nickname = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.user.username
