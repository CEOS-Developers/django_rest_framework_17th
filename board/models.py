from django.db import models
from global_entity.models import BaseModel, University
from account.models import User


# Create your models here.

class Board(BaseModel):
    board_id = models.IntegerField('primary key', primary_key=True)

    university = models.ForeignKey(University, on_delete=models.PROTECT)
    board_name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)


class Post(BaseModel):
    post_id = models.AutoField('primary key', primary_key=True)

    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    writer = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=512, null=False)
    is_deleted = models.BooleanField(default=False)
    is_anon = models.BooleanField(default=False)
    is_question = models.BooleanField(default=False)


class Comment(BaseModel):
    comment_id = models.AutoField('primary key', primary_key=True)

    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    writer = models.ForeignKey(User, on_delete=models.PROTECT)
    ancestor_comment = models.ForeignKey('self', on_delete=models.PROTECT)
    content = models.CharField(max_length=512)
    is_deleted = models.BooleanField(default=False)
    is_anon = models.BooleanField(default=False)


class PostUser(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    writer = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True  # Set this model as Abstract


class CommentUser(BaseModel):
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT)
    writer = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True  # Set this model as Abstract


class LikePost(PostUser):
    like_post_id = models.AutoField('primary key', primary_key=True)

    class Meta:
        db_table = 'like_post'


class ScrapPost(PostUser):
    scrap_post_id = models.AutoField('primary key', primary_key=True)

    class Meta:
        db_table = 'scrap_post'


class BlackPost(PostUser):
    black_post_id = models.AutoField('primary key', primary_key=True)

    class Meta:
        db_table = 'black_post'


class LikeComment(CommentUser):
    like_post_id = models.AutoField('primary key', primary_key=True)

    class Meta:
        db_table = 'like_comment'


class BlackComment(CommentUser):
    black_comment_id = models.AutoField('primary key', primary_key=True)

    class Meta:
        db_table = 'black_comment'
