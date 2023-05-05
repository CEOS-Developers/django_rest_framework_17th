from django.db import models
from django.contrib.auth.models import User
from utils.models import BaseModel


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


