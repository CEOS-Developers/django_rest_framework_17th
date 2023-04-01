from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    status = models.CharField(max_length=10, default='A')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.field_name


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=60)
    email = models.EmailField(max_length=60)
    password = models.TextField(max_length=200)
    profileImgPath = models.TextField(null=True)
    friends = models.ManyToManyField('self')


class School(BaseModel):
    name = models.TextField(max_length=60)
    campus = models.TextField(max_length=60, null=True)


class Board(BaseModel):
    name = models.TextField(max_length=60)
    school = models.ForeignKey("School", related_name="school", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)


class Post(BaseModel):
    board = models.ForeignKey("Board", related_name="board", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)
    title = models.TextField(max_length=100, null=True)
    contents = models.TextField(max_length=200)
    isAnonymous = models.CharField(max_length=10, default='Y')
    isQuestion = models.CharField(max_length=10, default='N')


class Photo(BaseModel):
    post = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE)
    path = models.TextField()


class Comment(BaseModel):
    post = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=0)
    contents = models.TextField(max_length=200)