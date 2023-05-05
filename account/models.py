from django.db import models
from django.contrib.auth.models import User
from utils.models import BaseModel
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, school_id=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=email,
            nickname=nickname,
            school_id=school_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, school_id=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            nickname=nickname,
            school_id=school_id,
            password=password,
        )
        superuser.is_admin = True
        superuser.save(using=self._db)
        return superuser


class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=100, unique=True)
    # password, last_login 은 기본 제공
    profile_img_path = models.URLField(blank=True, null=True)
    friends = models.ManyToManyField('self', blank=True, null=True)
    school = models.ForeignKey("School", on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    def __str__(self):
        return self.email


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img_path = models.URLField(blank=True)
    friends = models.ManyToManyField('self', blank=True)
    school = models.ForeignKey("School", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class School(BaseModel):
    name = models.CharField(max_length=60)
    campus = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name


