from django.db import models
from utils.models import BaseModel
from account.models import *


class Board(BaseModel):
    name = models.CharField(max_length=60)
    school = models.ForeignKey("account.School", on_delete=models.CASCADE)
    profile = models.ForeignKey("account.Profile", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(BaseModel):
    board = models.ForeignKey("Board", on_delete=models.CASCADE)
    profile = models.ForeignKey("account.Profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    contents = models.CharField(max_length=200)
    is_anonymous = models.CharField(max_length=10, default='Y')
    is_question = models.CharField(max_length=10, default='N')

    def __str__(self):
        return self.contents


class Photo(BaseModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    path = models.TextField()

    def __str__(self):
        return f"{self.path} included in {self.post}"


class Comment(BaseModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("account.Profile", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=0)
    contents = models.CharField(max_length=200)

    def __str__(self):
        return self.contents


class PostLike(BaseModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("account.Profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} 's like on {self.post}"


class CommentLike(BaseModel):
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    profile = models.ForeignKey("account.Profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} 's like on {self.comment}"


class Scrap(BaseModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("account.Profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} 's scrap of {self.post}"
