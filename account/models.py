from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    # 별명 필드
    nickname = models.CharField(max_length=50)

    # 학교 필드(외래키)
    # 정지 여부
    # 기간 필드
