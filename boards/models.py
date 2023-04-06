from django.db import models

from accounts.models import School, User
from bases.models import BaseTimeModel


# Create your models here.


class Board(BaseTimeModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='boards')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    allow_anony = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Post(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=30)
    content = models.TextField()
    like_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    is_delete = models.BooleanField(default=False)  # 댓글이 지워져도 대댓글들은 보이게
    like_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content


class CommentReply(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_replies')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_replies')
    content = models.TextField()
    like_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content


class PostLike(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')

    def __str__(self):
        return '{}번 게시글에 {}님의 공감'.format(self.post.id, self.user.username)


class CommentLike(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes')

    def __str__(self):
        return '{}번 댓글에 {}님의 공감'.format(self.comment.id, self.user.username)


class CommentReplyLike(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_reply_likes')
    comment_reply = models.ForeignKey(CommentReply, on_delete=models.CASCADE, related_name='comment_reply_likes')

    def __str__(self):
        return '{}번 대댓글에 {}님의 공감'.format(self.comment_reply.id, self.user.username)


class Scrap(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scraps')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='scraps')

    def __str__(self):
        return '{} 유저가 {}번 게시글 스크랩'.format(self.user.username, self.post.id)
