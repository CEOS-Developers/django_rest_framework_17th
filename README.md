# CEOS 17기 백엔드 스터디 - 2주차

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
  
<br>
    
# CEOS 17기 백엔드 스터디 - 3주차

### 1. 미션 설명
#### (1) API 명세서

<img width="909" alt="image" src="https://user-images.githubusercontent.com/77063375/230726711-1d65667e-40bb-4326-a75f-92f837b6ce19.png">

이번 미션은 간단한 crud api를 만드는 거였는데, 냅다 만들려니까 좀 헷갈려서 간단하게 api 명세서를 작성해보았다
- Board
  - 전체 게시판 조회(GET)
  - 전체 게시글 조회(GET)
  - 게시글 작성(POST)
  - 특정 게시글 조회(GET)
  - 특정 게시글 삭제(DELETE) -> 어디서 들었는지 기억이 나지 않는데, HTTP 메서드는 GET과 POST만 쓰는 것이 좋다고 스쳐지나가면서 들은 것 같다... 혹시 아시는 분...?
- Timetable
  - 특정 시간표 및 친구 리스트 조회(GET) -> 에브리타임 앱에서 시간표와 친구 리스트가 한 화면에 출력되길래 api 하나에 시간표와 친구 리스트 데이터를 같이 반환하고자 했다
  - 시간표 생성(POST)
  - 특정 시간표 삭제(DELETE)
  - 강의 검색(GET)
  
 #### (2) API View
 Django에서 view를 만드는 방법은 FBV(Function-Based View)와 CBV(Class-Based View) 두 가지 방법이 있다
 
 두 가지 중 어떤 것이 정답이다라고는 말할 수 없지만, 대체적으로 확장성과 재사용성이 낮다는 FBV의 단점을 보완한 CBV를 많이 쓴다고 한다
 
 이번 미션은 우선 CBV로 view를 작성한 후, ViewSet으로 리팩토링 하는 것이었다
 
 하지만 CBV로 코드 짜는 것에 시간을 많이 투자하느라 ViewSet으로 바꾸는 것에 소홀해져버렸다ㅠㅠ
 
 ~~~python
 class PostList(APIView):
	def get(self, request, board_id, format=None):
		post_list = Post.objects.filter(board__id=board_id)
		serializer = PostListSerializer(post_list, many=True)
		return Response(serializer.data, status=200)

	def post(self, request, board_id, format=None):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(board_id=board_id)
			return Response(status=201)
		return Response(serializer.errors, status=400)


class PostDetail(APIView):
	def get_object(self, post_id):
		try:
			return Post.objects.get(id=post_id)
		except Post.DoesNotExist:
			raise Http404("존재하지 않는 게시글입니다.")

	def get(self, request, board_id, post_id, format=None):
		post = self.get_object(post_id)
		serializer = PostSerializer(post)
		return Response(serializer.data, status=200)

	def delete(self, request, board_id, post_id, format=None):
		post = self.get_object(post_id)
		post.delete()
		return Response(status=204)
~~~

위의 코드와 같이 Django Rest Framework 에서 만든 API View를 상속하여 CBV를 작성했다

~~~python
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['school_id']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
~~~

그리고 이렇게 ViewSet과 filter를 사용하여 리팩토링했다
너무 편리한 기능이어서 오히려 불안하다
이렇게 해도 잘 돌아가?
근데 잘 돌아가더라...하하

#### (3) API 테스트
<img width="1919" alt="image" src="https://user-images.githubusercontent.com/77063375/230727214-74f72ff4-f530-4387-85a2-2c0d534b5788.png">
<img width="1919" alt="image" src="https://user-images.githubusercontent.com/77063375/230727240-8ddaf0c8-1163-4683-9b59-774afc107102.png">

우선 GET과 DELETE 요청은 제대로 응답이 온다 POST는... 이제부터 설명하겠다^^

<br>

### 2. 겪은 오류와 해결 과정

정말정말 많은 오류들을 겪었는뎅... 하 큰 것들만 몇 개 적어보겠다

#### (1) ManyToManyField가 있는 Model의 POST 요청 오류
<img width="1919" alt="image" src="https://user-images.githubusercontent.com/77063375/230727421-c1e25a5b-77bb-4e9b-9952-132f2dad09fd.png">

Timetable 모델은 CourseDetail 모델과 다대다로 연결되어있다

근데 Timetable 모델에 POST 요청을 통해 데이터를 저장하려고 하니까 자꾸 위의 사진처럼 응답이 왔다

courses 필드는 null 허용으로 처리해주고, 빈 리스트로 삽입하고, 진짜 데이터를 넣어보고, 별 짓을 다해봤는데도 해결이 안 된다

어떻게 하는 건가요...!!!! 흑

#### (2) ViewSet 리팩토링 과정에서 url router의 basename 오류
<img width="1919" alt="image" src="https://user-images.githubusercontent.com/77063375/230727739-a65359a8-7ff1-43da-8a41-24a7c0d437fc.png">
ViewSet으로 리팩토링하다가 이런 오류가 발생했따 결국 해결 못 해서 timetables 앱은 리팩토링을 못 했따...ㅠ 시험기간 끝나고 천천히 다시 해봐야겠다

#### (3) AbstractUser 상속 오류
저번 주 미션에서 상속하고 관리자가 만들어지지 않는 오류를 겪었는데

user의 school_id 필드에 null 허용 해줬더니 정상 작동되었다

관리자도 user 모델 기반으로 만들어지니, createsuperuser 명령어를 통해 만들 때 school_id 값이 당연히 들어가지 않으니 발생한 오류였다(꼼꼼히 보자!!!!)

그 외 자잘한 오류들은 구글링 + 머리싸매기로 해결했다 하하

<br>

### 4. 궁금한 점
~~~python
# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boards.urls')),
    path('timetables/', include('timetables.urls'))
]


# timetable.urls.py
router = routers.DefaultRouter()
router.register('', TimetableViewSet)
router.register('courses', CourseViewSet)
~~~
ViewSet으로 리팩토링하면서 urls에 router를 추가해주다가 궁금한 것이 생겼다

나는 'timetable/courses/'라는 api를 만들고 싶어서 이것저것 해보다가 실패했는데,

router 간에 계층 구조(?)를 만들 수는 없는 것일까?


<br>

### 4. 회고
간단한 crud api 만들기라고 해서 만만하게 봤는데 정말정말 힘들었다

api를 어떻게 짤까 고민을 많이 했는데, 살면서 가장 에브리타임에 많이 접속한 것 같다

그리고 API 명세서를 기껏 짜놓았는데 ViewSet으로 리팩토링하다가 보니까 url 구조가 다 망가졌다

다음에 각 잡고 다시 짜봐야겠다

그리고 3주 동안 Django로 끄적끄적 해본 소감

편리하다. 편리한데...ㅠㅠ

개발자 편리하라고 이것저것 다 제공해주는데, 이걸 위해서 많은 것을 정형화 해놓은 것 같다

편리한 대신 자유도가 낮은 느낌? 아직 내가 익숙하지 않아서 그런 거겠지^^?

Django로 개발 경험이 있는 친구에게 내 코드를 보여주니까 왜 이렇게 스프링 같이 코드를 짜냐고 했다

아직까지 장고는 갈피를 못 잡고 있는 거 같다 ^_ㅠ...




 
 
  
  


