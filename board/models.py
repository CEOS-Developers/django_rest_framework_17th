from django.db import models
from global_entity.models import BaseModel, University
from account.models import User


# Create your models here.

class Board(BaseModel):
    board_id = models.AutoField('primary key', primary_key=True)

    university = models.ForeignKey(University, on_delete=models.PROTECT)
    board_name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.university.univ_name} : {self.board_name}'


class Post(BaseModel):
    post_id = models.AutoField('primary key', primary_key=True)

    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    writer = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=512, null=False)
    is_deleted = models.BooleanField(default=False)
    is_anon = models.BooleanField(default=False)
    is_question = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} : {self.writer.nickname}'


class Message(BaseModel):
    message_id = models.AutoField('primary key', primary_key=True)

    from_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='to_user')

    content = models.CharField(max_length=256)

    def __str__(self):
        return f'mesage from {self.from_user.nickname} to {self.to_user.nickname} : {self.content}'


class Friendship(BaseModel):
    friendship_id = models.AutoField('primary key', primary_key=True)

    from_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='friend_one')
    to_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='friend_two')

    def __str__(self):
        return f'mesage from {self.from_user.nickname} to {self.to_user.nickname}'


class Comment(BaseModel):
    comment_id = models.AutoField('primary key', primary_key=True)

    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    writer = models.ForeignKey(User, on_delete=models.PROTECT)
    ancestor_comment = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    content = models.CharField(max_length=512)
    is_deleted = models.BooleanField(default=False)
    is_anon = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.content} : {self.writer.nickname}'


class PostUser(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    who = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True  # Set this model as Abstract


class CommentUser(BaseModel):
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT)
    who = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True  # Set this model as Abstract


class LikePost(PostUser):
    like_post_id = models.AutoField('primary key', primary_key=True)

    class Meta:
        db_table = 'like_post'

    def __str__(self):
        return f'like {self.post.title} : {self.who.nickname}'


class ScrapPost(PostUser):
    scrap_post_id = models.AutoField('primary key', primary_key=True)

    class Meta:
        db_table = 'scrap_post'

    def __str__(self):
        return f'scrap {self.post.title} : {self.who.nickname}'


class BlackPost(PostUser):
    black_post_id = models.AutoField('primary key', primary_key=True)

    class Meta:
        db_table = 'black_post'

    def __str__(self):
        return f'black {self.post.title} : {self.who.nickname}'


class LikeComment(CommentUser):
    like_post_id = models.AutoField('primary key', primary_key=True)

    class Meta:
        db_table = 'like_comment'

    def __str__(self):
        return f'like {self.comment.content} : {self.who.nickname}'


class BlackComment(CommentUser):
    black_comment_id = models.AutoField('primary key', primary_key=True)

    class Meta:
        db_table = 'black_comment'

    def __str__(self):
        return f'black {self.comment.content} : {self.who.nickname}'
