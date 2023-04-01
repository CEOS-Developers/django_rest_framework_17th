# CEOS 17기 백엔드 스터디

### 1. 서비스 설명

#### (1) 에브리타임의 모든 기능을 파악해 모델을 작성하지는 못 했지만, 유저, 커뮤니티, 시간표 기능의 모델들을 구현하였다
  - 유저는 회원가입시 학교를 선택할 수 있다
  - 학교 별로 게시판들이 따로 존재하며 각 게시판에 게시글을 작성할 수 있다
  - 게시글에 댓글, 대댓글도 작성 및 공감 할 수 있다
  - 필요한 게시글을 스크랩하여 확인할 수 있다
  - 시간표를 만들 수 있으며 친구의 시간표도 확인할 수 있다
  
  ![everytime (2)](https://user-images.githubusercontent.com/77063375/229275237-279b9792-555f-4ad4-8f53-277dc2f93771.png)

#### (2) 구현 모델
  - 유저 기본 정보: User, School
  - 커뮤니티 기능: Board, Post, Comment, CommentReply, PostLike, CommentLike, CommentReplyLike, Scrap
  - 시간표 기능: Timetable, TimetableCourse, CourseDetail, Course, Friend

<br></br>

### 2. 미션 결과

<img width="1470" alt="Screen Shot 2023-04-01 at 4 44 18 PM" src="https://user-images.githubusercontent.com/77063375/229275366-0523ef50-3f6b-4c1e-83d1-1ac4aa947e89.png">

#### (1) 데이터베이스에 해당 모델 객체 3개 이상 넣기: 
user를 ForeignKey로 연결하여 timetable 객체를 3개 만들었다
#### (2) 삽입한 객체들을 쿼리셋으로 조회해보기 (단, 객체들이 객체의 특성을 나타내는 구분가능한 이름으로 보여야 함):
`Timetable.objects.all()` 로 만들어진 Timetable 객체들을 조회해보았다
#### (3) filter 함수 사용해보기:
`Timetable.objects.filter(user__nickname=”haen-su”)`로 유저의 닉네임으로 timetable을 조회해보았다

<br></br>

### 3. 겪은 오류와 해결 과정
#### (1) AbstractUser 상속 후 makemigration 오류
  - Django에서 기본으로 제공하는 User 모델을 확장하기 위한 방법은 3가지가 있다
    - 기본 User 모델을 OneToOneField 방식으로 연결하여 확장
    - AbstractUser 상속
    - AbstractBaseUser 상속
  - AbstractBaseUser를 상속받는 것이 가장 User 모델 필드를 자유롭게 구성할 수 있지만, 이 미션에서는 간단하게 OneToOneField 방식이나 AbstractUser를 상속 받으려고 하였다
  - 찾아보니 OneToOneField 방식이 가장 간단하지만 추가 쿼리를 발생시키는 문제점이 있다고 한다
  - 그래서 AbstractUser를 상속하는 User 모델을 작성하였다
            
```python
  from django.contrib.auth.models import AbstractUser
            
  class User(AbstractUser, BaseTimeModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='users')
    nickname = models.CharField(max_length=10, unique=True)
            
    def __str__(self):
      return self.nickname
```
  - 하지만 makemigrations 명령어 실행시 다음과 같은 오류가 발생하였다
<img width="1492" alt="Untitled" src="https://user-images.githubusercontent.com/77063375/229275529-cb8773c7-fa71-4c00-ab27-9e653d438d89.png">
            
  - 찾아보니 기본 User 모델을 명시해주지 않아서 발생한 오류
  - [setting.py](http://setting.py) 에 `AUTH_USER_MODEL = 'api.User'` 추가로 해결하였다
#### (2) AbstractUser 상속 후 createsuperuser 오류
  - makemigrations 문제를 해결하여 migration을 DB에 정상적으로 반영함
  - 이후 서버를 실행하고, 관리자 페이지를 생성하기 위해 `python manage.py createsuperuser` 명령어를 실행하니 IntegrityError에서 School 모델의 school_id 필드가 null이 될 수 없다는 오류가 발생하였다
  - 계속 찾아보니 AbstractUser 모델을 상속 받으면서 생긴 문제인 것 같아 DB 초기화, migration 초기화 등 여러 방법으로 해결하려고 시도해보았으나 해결하지 못 해서 결국 OneToOneField로 User 모델을 확장하는 방법으로 바꾸었다 …
    
<br></br>

### 4. 새롭게 배운 점

- ManyToManyField를 사용하여 모델을 다대다 관계로 연결하면 Django가 자동으로 중간 테이블을 만들어 다대다 관계를 풀어준다
- ORM 문법: `Timetable.objects.filter(user__nickname="haen-su")` 이와 같이 외래키로 연결된 필드의 값으로 filter 명령어를 사용하려면 언더바 두 개를 사용해야한다
- 클래스 내에 `Meta` 라는 클래스를 선언하여 모델의 속성을 정의할 수 있음 본 미션에서는 `abstract=True`를 통해 추상클래스라는 것을 명시해준다
- choices 기능을 통해 선택지를 추가할 수 있다
    
    ```python
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
    
        # 1~15교시 선택
        TIME_CHOICES = [
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
    ```
    
<br></br>

### 5. 회고
    
    Django로 처음 직접 에브리타임 모델링을 해 보았다
    
    평소에는 당연하게 생각했던 기능들인데, 실제로 모델링을 하려니 굉장히 많은 기능들이 있고 복잡하다는 것을 깨달았다
    
    시간적 여유가 부족하여 구체적으로 구현하지는 못 한 게 아쉽다
    
    이번 미션을 진행하면서 조금이나마 Django에 익숙해질 수 있었다
