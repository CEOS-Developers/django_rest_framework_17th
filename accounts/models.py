from django.contrib.auth.models import AbstractUser
from django.db import models

from bases.models import BaseTimeModel


# Create your models here.


class School(BaseTimeModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class User(AbstractUser, BaseTimeModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='users', null=True)
    nickname = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.username
