from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    status = models.CharField(max_length=10, default='A')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=200)
    profileImgPath = models.TextField(null=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.nickname


class School(BaseModel):
    name = models.CharField(max_length=60)
    campus = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.name


class Board(BaseModel):
    name = models.CharField(max_length=60)
    school = models.ForeignKey("School", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(BaseModel):
    board = models.ForeignKey("Board", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    contents = models.CharField(max_length=200)
    isAnonymous = models.CharField(max_length=10, default='Y')
    isQuestion = models.CharField(max_length=10, default='N')

    def __str__(self):
        return self.contents


class Photo(BaseModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    path = models.TextField()

    def __str__(self):
        return f"{self.path} included in {self.post}"


class Comment(BaseModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=0)
    contents = models.CharField(max_length=200)

    def __str__(self):
        return self.contents


class PostLike(BaseModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} 's like on {self.post}"


class CommentLike(BaseModel):
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} 's like on {self.comment}"


class Scrap(BaseModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} 's scrap of {self.post}"


class TimeTable(BaseModel):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class LectureDomain(BaseModel):
    name = models.CharField(max_length=60)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name


class Lecture(BaseModel):
    name = models.CharField(max_length=150)
    lectureDomain = models.ForeignKey("LectureDomain", on_delete=models.CASCADE, null=True)
    collegeYear = models.CharField(max_length=10, default='0')
    credit = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    lectureCode = models.CharField(max_length=60)
    classRoom = models.CharField(max_length=100)
    dayAndTime = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TakeLecture(BaseModel):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    lecture = models.ForeignKey("Lecture", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} started taking {self.lecture}"


class LectureReview(BaseModel):
    lecture = models.ForeignKey("Lecture", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    rating = models.CharField(max_length=10)
    contents = models.CharField(max_length=200)

    def __str__(self):
        return self.contents


class ReviewLike(BaseModel):
    lectureReview = models.ForeignKey("LectureReview", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", related_name="profiles", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} 's like on {self.lectureReview}"
