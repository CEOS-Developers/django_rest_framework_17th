from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from bases.models import BaseTimeModel


class School(BaseTimeModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, username, email, nickname, password=None):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not username:
            raise ValueError(_('Users must have an ID'))

        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            nickname=nickname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, nickname, password):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            nickname=nickname,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, BaseTimeModel, PermissionsMixin):
    username = models.CharField(max_length=15, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='users', null=True)
    nickname = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=10)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname', 'email']

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.username
