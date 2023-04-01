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
    nickname = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=200)
    profileImgPath = models.TextField(null=True)
    friends = models.ManyToManyField('self')


class School(BaseModel):
    name = models.CharField(max_length=60)
    campus = models.CharField(max_length=60, null=True)


class Board(BaseModel):
    name = models.CharField(max_length=60)
    school = models.ForeignKey("School", related_name="school", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)


class Post(BaseModel):
    board = models.ForeignKey("Board", related_name="board", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    contents = models.CharField(max_length=200)
    isAnonymous = models.CharField(max_length=10, default='Y')
    isQuestion = models.CharField(max_length=10, default='N')


class Photo(BaseModel):
    post = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE)
    path = models.TextField()


class Comment(BaseModel):
    post = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=0)
    contents = models.CharField(max_length=200)


class PostLike(BaseModel):
    post = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)


class CommentLike(BaseModel):
    comment = models.ForeignKey("Comment", related_name="post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)


class Scrap(BaseModel):
    post = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)


class TimeTable(BaseModel):
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)


class LectureDomain(BaseModel):
    name = models.CharField(max_length=60)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=0)


class Lecture(BaseModel):
    lectureDomain = models.ForeignKey("LectureDomain", related_name="lectureDomain", on_delete=models.CASCADE, null=True)
    collegeYear = models.CharField(max_length=10, default='0')
    credit = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    lectureCode = models.CharField(max_length=60)
    classRoom = models.CharField(max_length=100)
    dayAndTime = models.CharField(max_length=100)


class TakeLecture(BaseModel):
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)
    lecture = models.ForeignKey("Lecture", related_name="lecture", on_delete=models.CASCADE)


class LectureReview(BaseModel):
    lecture = models.ForeignKey("Lecture", related_name="lecture", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)
    rating = models.CharField(max_length=10)
    contents = models.CharField(max_length=200)


class ReviewLike(BaseModel):
    lectureReview = models.ForeignKey("LectureReview", related_name="lectureReview", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profile", on_delete=models.CASCADE)