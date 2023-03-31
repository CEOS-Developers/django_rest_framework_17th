from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    login_id = models.CharField(max_length=255, unique=True)
    univ = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True)
    profile_image = models.TextField(null=True)
    is_superuser = models.BooleanField(default=False)
    first_name = None
    last_name = None
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Board(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FriendList(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proposer')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')

    def __str__(self):
        return '{} to {}'.format(self.user.username, self.friend.username)


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    like_number = int
    image1 = models.TextField(null=True)
    image2 = models.TextField(null=True)
    image3 = models.TextField(null=True)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    like_number = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class Reply(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    like_number = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class CourseInfo(BaseModel):
    course_name = models.CharField(max_length=255)
    professor = models.CharField(max_length=255)

    class Meta:
        db_table = 'CourseInfo'
        unique_together = (('course_name', 'professor'),)

    def __str__(self):
        return '{} of {}'.format(self.course_name, self.professor)


# class Classroom(BaseModel):
#     class_field = models.CharField(max_length=255)
#
#
# class Time(BaseModel):
#     day = models.CharField(max_length=255)
#     period = models.CharField(max_length=255)


class Course(BaseModel):
    course_info = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    # classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # time = models.ForeignKey(Time, on_delete=models.CASCADE)
    year_semester = models.CharField(max_length=255)
    credits = models.IntegerField()
    course_number = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    classroom = models.CharField(max_length=255)

    def __str__(self):
        return '{} of {}'.format(self.course_info.course_name, self.course_number)


class Timetable(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return '{} take {}'.format(self.user.username, self.course.course_info.course_name)


class Review(BaseModel):
    course_info = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    score = models.IntegerField()
    content = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)

    def __str__(self):
        return self.content
