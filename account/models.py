from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractBaseUser):
    login_id = models.CharField(max_length=30, unique=True, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False)
    univ = models.CharField(max_length=255)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    profile_image = models.URLField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'login_id'

    def __str__(self):
        return self.username


class FriendList(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proposer')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')

    def __str__(self):
        return '{} to {}'.format(self.user.username, self.friend.username)

