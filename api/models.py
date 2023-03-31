from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BaseTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class School(BaseTimeModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='users')
    nickname = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.user.username


class Board(BaseTimeModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='boards')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    allow_anony = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Post(BaseTimeModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=30)
    content = models.TextField()
    like_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(BaseTimeModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    is_delete = models.BooleanField(default=False)  # 댓글이 지워져도 대댓글들은 보이게
    like_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content


class CommentReply(BaseTimeModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment_replies')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_replies')
    content = models.TextField()
    like_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content


class PostLike(BaseTimeModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')

    def __str__(self):
        return '{}번 게시글에 {}님의 공감'.format(self.post.id, self.user.user.username)


class CommentLike(BaseTimeModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment_likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes')

    def __str__(self):
        return '{}번 댓글에 {}님의 공감'.format(self.comment.id, self.user.user.username)


class CommentReplyLike(BaseTimeModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment_reply_likes')
    comment_reply = models.ForeignKey(CommentReply, on_delete=models.CASCADE, related_name='comment_reply_likes')

    def __str__(self):
        return '{}번 대댓글에 {}님의 공감'.format(self.comment_reply.id, self.user.user.username)


class Scrap(BaseTimeModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='scraps')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='scraps')

    def __str__(self):
        return '{} 유저가 {}번 게시글 스크랩'.format(self.user.username, self.post.id)


class Timetable(BaseTimeModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='timetables')
    name = models.CharField(max_length=10)
    course = models.ManyToManyField('CourseDetail')

    def __str__(self):
        return self.name


class Course(BaseTimeModel):
    title = models.CharField(max_length=20)
    professor = models.CharField(max_length=20)
    credit = models.IntegerField()
    hours = models.IntegerField()

    def __str__(self):
        return '{}-{}'.format(self.title, self.professor)


class CourseDetail(BaseTimeModel):
    MON = '월'
    TUE = '화'
    WED = '수'
    THU = '목'
    FRI = '금'
    SAT = '토'
    SUN = '일'

    DAY_CHOICES = [
        (MON, '월'),
        (TUE, '화'),
        (WED, '수'),
        (THU, '목'),
        (FRI, '금'),
        (SAT, '토'),
        (SUN, '일')
    ]

    TIME_CHOICES = [    # 1~15교시 선택
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15)
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_details')
    course_code = models.CharField(max_length=10)
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    time = models.IntegerField(choices=TIME_CHOICES)
    hours = models.IntegerField(default=1)
    classroom = models.CharField(max_length=10)

    def __str__(self):
        return self.course_code


class Friend(BaseTimeModel):
    from_user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friend')
    to_user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friend_list')
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.id
