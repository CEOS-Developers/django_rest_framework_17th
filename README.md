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

<br>
<br>

# CEOS 백엔드 스터디 - 4주차

> 이번 주 미션은 로그인 인증에 대해서 알아보고 Django에서 지원하는 Simple JWT로 직접 로그인을 구현해보는 것이다!

<br>

## 1. 로그인 인증은 어떻게 하나요?
### (1) 세션과 쿠키를 이용한 인증

#### 인증 방법
- 사용자가 로그인을 하면 서버에서 사용자를 확인한 후, 사용자에게 고유한 ID값을 부여하여 세션 저장소에 저장하고 `Session ID`를 발급한다

- 서버는 HTTP response header에 발급된 `Session ID`를 넣어 보낸다
클라이언트는 매 요청마다 HTTP request header에 `Session ID`가 담킨 쿠키를 보낸다

- 서버에서는 세션 저장소에서 받은 쿠키와 일치하는 정보를 가져와 인증을 한다


#### 장점
- 사용자의 정보는 세션 저장소에 저장되기 때문에 쿠키가 노출되더라도 사용자의 정보는 알 수 없다

- 사용자는 고유의 `Session ID`를 가지므로 회원 정보를 하나씩 대조할 필요가 없어 서버 자원 낭비를 줄일 수 있다

#### 단점
- 노출된 쿠키를 사용하여 서버로 HTTP 요청을 보내 서버가 사용자로 오인해 정보를 전달하게 만드는 세션 하이재킹 공격에 취약하다

- 세션 저장소를 사용하기 때문에 추가적인 저장공간을 필요로 한다

<br>

### (2) Access Token을 이용한 인증

#### 인증 방법

- 사용자가 로그인을 하면 서버에서 사용자를 확인 후, `Payload`에 사용자의 정보를 넣는다

- 암호화된 `Access Token`을 HTTP response header에 넣어 보낸다

- 사용자는 `Access Token`을 받아 저장한 후, 인증이 필요한 요청마다 토큰을 HTTP request header에 넣어 보낸다

- 서버에서는 해당 토큰의 `Verify Signature`를 복호화한 후, 조작 여부와 토큰 유효 기간을 확인한다

- 검증이 완료된다면, `Payload`를 디코딩하여 사용자의 정보에 맞는 데이터를 가져온다

#### 장점

- 유저 정보를 토큰에 저장하므로 서버에 따로 추가 저장 공간이 필요 없다 -> 메모리, 비용 절감

- 토큰 기반으로 하는 다른 인증 시스템에 접근이 가능하기 때문에 확장성이 뛰어나다

#### 단점

- JWT는 한 번 발급되면 유효기간이 만료될 때까지 삭제가 불가능하므로 한번 노출되면 대처할 방안이 없다

- `Payload`는 디코딩하면 누구나 접근할 수 있기에 중요한 정보들을 보관할 수 없다

- JWT는 길기 때문에 인증 요청이 많아지면 서버에 자원낭비가 발생한다

<br>

### (3) Access Token + Refresh Token을 이용한 인증

Access Token을 이용한 인증 방식의 문제는 토큰이 노출될시 대처 방안이 없다는 것이다
토큰의 유효기간을 짧게 하면 사용자는 로그인을 자주 해야해서 번거롭기에 이를 해결하고자 나온 것이 `Refresh Token`이다

`Refresh Token`은 `Access Token`과 같은 형태인 JWT이다
`Refresh Token`은 `Access Token`보다 유효기간이 길며, `Access Token`이 만료됐을 때 `Refresh Token`을 통해 `Access Token`을 재발급 할 수 있다

#### 인증 방법

- 사용자가 로그인을 하면 `Access Token`, `Refresh Token`을 발급하여 HTTP response header에 넣어 보낸다 Refresh Token은 따로 사용자 DB에 저장해놓는다

- 사용자는 `Refresh Token`은 안전한 저장소에 저장 후, 요청을 보낼 때 `Access Token`을 HTTP request header에 넣어 보낸다

- 서버는 받은 `Access Token`을 검증한다 이때 유효기간이 지나 `Access Token`이 만료됐다면 권한 없음을 HTTP 응답으로 보낸다

- 권한 없음 응답을 받은 사용자는 `Refresh Token`과 `Access Token`을 함께 HTTP request header에 보낸다

- 서버는 받은 `Access Token`을 검증한 후, 받은 `Refresh Token`과 사용자의 DB에 저장되어 있던 Refresh Token을 비교한다

- `Refresh Token`이 동일하고 유효기간도 지나지 않았다면 새로운 `Access Token`을 발급하여 HTTP response header로 보낸다

#### 장점
- `Access Token`의 유효 기간이 짧기 때문에, 기존의 `Access Token`만을 이용한 인증보다 안전하다

#### 단점
- `Access Token`만 사용하는 것 보다 구현이 복잡하다

- `Access Token`이 만료될 때마다 새롭게 발급하는 과정에서 서버의 자원 낭비가 생긴다

<br>

### (4) OAuth를 이용한 인증

OAuth는 외부서비스의 인증 및 권한부여를 관리하는 범용적인 프로토콜이다
현재 범용적으로 사용되고 있는 것은 OAuth 2.0이다

<br>
<br>

## 2. JWT
### (1) JWT란?

`JSON Web Token(JWT)`는 인증에 필요한 정보들을 암호화시킨 토큰으로, 당사자 간에 정보를 JSON 형태로 안전하게 전송할 수 있다
이는 `Access Token`으로 사용된다

<br>

### (2) JWT의 구성

JWT를 생성하기 위해서는 `Header`, `Payload`, `Verify Signature` 객체가 필요하다 

<br>

**<Header\>**
`Header`는 `alg`와 `typ`로 구성된다
- `alg`: 암호화 방식(해싱 알고리즘)
- `typ`: 토큰의 타입

```js
{
  'alg': 'HS256',
  'typ': 'JWT'
}
```
<br>

**<Payload\>**
`Payload`는 토큰에 담을 정보를 나타낸다
하나의 정보 조각을 클레임(Claims)으로 부르는데, 클레임의 종류로는 `Registered`, `Public`, `Private`로 3가지가 존재한다

- `Registered Claims`(필수는 아닌 이름이 지정되어 있는 클레임들):

    - iss: JWT의 발급자 주체, 대소문자를 구분하는 문자열
    
    - sub: JWT의 제목
    
    - aud: JWT의 수신인, JWT를 처리하려는 주체는 해당 값으로 자신을 식별해야함(요청 처리의 주체가 aud 값으로 자신을 식별하지 않으면 JWT는 거부됨)
        
    - exp: JWT의 만료시간 설정(NumericDate 형식)
    
    - nbf: Not Before을 의미
    
    - iat: JWT가 발급된 시간
    
    - jti: JWT의 식별자 값 (JWT ID), 중복 처리를 방지하기 위해 사용
    
- `Public Claims`: 키와 값을 마음대로 정의 가능(충돌이 발생하지 않을 이름으로 설정해야함)

- `Private Claims`: 통신 간에 상호 합의되고 등록된 클레임과 공개된 클레임이 아닌 클레임

```
{
  'sub': 'ceos payload',
  'name': 'haensu',
  'admin': true,
  'iat': 1516239022
}
```

<br>

**<Verify Signature\>**
`Payload`가 위변조되지 않았다는 사실을 증명하는 문자열이다 
`Base64Url` 방식으로 인코딩한 `Header`, `Payload` 그리고 `secret key`를 더한 후 암호화된다

<br>

완성된 토큰은 `<Header\>.<Payload\>.<Signature\>`의 형식을 가진다
`Header`와 `Payload`는 인코딩될 뿐, 따로 암호화되지 않기에 누구나 디코딩하여 확인할 수 있기에 정보가 쉽게 노출될 수 있다
하지만 Verify Signature는 `secret key`를 알지 못하면 복호화할 수 없다

만약에 해커가 사용자의 토큰을 훔쳐 Payload의 데이터를 변경하여 토큰을 서버로 보낸다면, 서버에서 Verify Signature를 검사하여 토큰의 유효성을 판단한다


<br>
<br>

## 3. Django Simple JWT

이제 직접 JWT를 이용한 인증을 구현해보겠다!
Django에서는 JWT 인증을 위해 `Simple JWT`라는 라이브러리를 제공한다

### (1) Simple JWT 설치 및 설정

```bash
pip install djangorestframework-simplejwt
```

위 명령어를 통해 라이브러리를 설치해주고

```python
INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
	...
]

...

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}

...

# 추가적인 JWT_AUTH 설정
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

AUTH_USER_MODEL = 'accounts.User'
```

`setting.py`에 다음과 같이 추가한다
`SIMPLE_JWT`에서는 토큰의 유효시간 등을 설정할 수 있다
`freeze` 명령어로 `requirements.txt`에 라이브러리 추가하는 거 잊지 말자!

<br>

#### (2) User Model 커스텀

JWT 인증을 사용하기 위해서는 `AbstractBaseUser` 모델을 상속하여 기본 유저 모델을 만들어야 한다
이전에는 `AbstractUser` 모델을 상속했었기에
DB랑 마이그레이션 모두 날리고 다시 만들었다 ㅠ

```python
class UserManager(BaseUserManager):
    def create_user(self, username, email, nickname, password=None):
        if not username:
            raise ValueError(_('Users must have an ID'))

        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            nickname=nickname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, nickname, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            nickname=nickname,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, BaseTimeModel, PermissionsMixin):
    username = models.CharField(max_length=15, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='users', null=True)
    nickname = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=10)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname', 'email']

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.username
```

<br>

#### (3) 회원가입/로그인/로그아웃 구현

회원 가입 후 로그인을 성공하면 Access Token과 Refresh Token을 모두 발급해주는 로직으로 구현하였다

![](https://velog.velcdn.com/images/haen/post/641707e3-0e11-4018-b547-f4297f1ffea8/image.png)
회원가입시 password가 암호화되어 DB에 저장된다


```python
class SignIn(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        # ID가 존재하지 않는 경우
        if user is None:
            return Response(
                {"message": "회원정보가 일치하지 않습니다"}, status=status.HTTP_400_BAD_REQUEST
            )

        # # 비밀번호가 틀린 경우
        if not check_password(password, user.password):
            return Response(
                {"message": "비밀번호가 틀렸습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        # user가 맞다면,
        if user is not None:
            token = TokenObtainPairSerializer.get_token(user)  # refresh 토큰 생성
            refresh_token = str(token)  # refresh 토큰 문자열화
            access_token = str(token.access_token)  # access 토큰 문자열화
            response = Response(
                {
                    "user": UserSerializer(user).data,
                    "message": "login success",
                    "jwt_token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token
                    },
                },
                status=status.HTTP_200_OK
            )

            response.set_cookie("access_token", access_token, httponly=True)
            response.set_cookie("refresh_token", refresh_token, httponly=True)
            return response
        else:
            return Response(
                {"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
            )
```

- `TokenObtainPairSerializer.get_token(user)`은 Simple JWT의 내장 Serializer이다 이를 통해 `Refresh Token`을 생성한다

- `check_password(current_password,user.password)`를 통해 hash 암호화 되어 저장된 password와 클라이언트로부터 받은 password를 비교하여 boolean값을 return해준다
      
- `response.set_cookie()'`를 통해 `Access Token`과 `Refresh Token`을 쿠키에 저장한다



![](https://velog.velcdn.com/images/haen/post/0066b830-b786-4963-afd2-837cc165cf12/image.png)

로그인 성공시 `Access Token`과 `Refresh Token`이 쿠키에 저장되는 것을 볼 수 있다


![](https://velog.velcdn.com/images/haen/post/4a326c14-b23d-469d-8af5-dd6233f6718f/image.png)

로그아웃시 쿠키에서 token이 삭제된다

<br>

#### (4) Access Token 재발급

`simple-jwt` 라이브러리에서 `Refresh Token`으로 `Access Token`을 재발급 해주는 뷰를 제공해준다

```python
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import SignUp, SignIn, Logout

urlpatterns = [
    path("sign-up/", SignUp.as_view()),
    path("sign-in/", SignIn.as_view()),
    path("log-out/", Logout.as_view()),
    path("refresh/", TokenRefreshView.as_view())
]
```

![](https://velog.velcdn.com/images/haen/post/806d6e63-2077-49fb-a1f5-973993b40080/image.png)

위와 같이 제대로 발급되는 것을 볼 수 있다!

<br>

## 4. Permission

이제 권한 설정을 구현해보겠다
에브리타임을 이용하기 위해서는 로그인이 필수이다 
즉, 로그인 하지 않은 사용자가 회원가입, 로그인 이외의 url에 접근하는 것을 막아야한다

로그인 했다는 것을 판별하기 위해 HTTP request header에 `Access Token`을 함께 보낸다
`Access Token`이 존재하지 않으면 해당 url에 접근할 수 없다
그럼 구현해보자!



```bash
pip install dj-rest-auth
```

우선 위의 명령어를 통해 라이브러리를 설치해준다

```python
INSTALLED_APPS = [
	...
    'dj_rest_auth',
    'rest_framework.authtoken',
	...
]

REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # )
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```
`DEFAULT_PERMISSION_CLASSES`를 `IsAuthenticated`로 설정했다

그리고 토큰 인증이 필요없는 회원가입, 로그인 뷰에는 

```python
permission_classes = [AllowAny]
```
접근 권한을 AllowAny로 설정해주었다


![](https://velog.velcdn.com/images/haen/post/00b893db-df9f-4aed-ac7f-126029d84703/image.png)

Postman에서 새로운 environments를 추가했고

![](https://velog.velcdn.com/images/haen/post/edca07ab-0cb2-4367-a758-73b7ecadc492/image.png)

로그인 API 테스트에서 로그인시 발급받은 `Access Token`이 자동으로 환경변수에 등록되도록 했다

![](https://velog.velcdn.com/images/haen/post/f7d50408-a213-488a-a8fb-5255eec6c839/image.png)

마지막으로 Authorization에서 Bearer Token을 환경 변수로 설정해주면 끝!

![](https://velog.velcdn.com/images/haen/post/7e9882b4-3fd2-48ce-84a3-1725654961e2/image.png)

로그인 하지 않았을 때 접근할 수 없다

![](https://velog.velcdn.com/images/haen/post/ac63c0b2-93b5-47f1-81ca-4baa6e3fc8d4/image.png)

로그인 하면 이렇게 접근 허용~~

<br>
<br>

### 5. 회고

저번 과제에서 ViewSet 리팩토링에서 났던 오류들을 수정하는 것이 조금 힘들었지만,
JWT로 인증 구현하는 것은 재미있었다!

<br>
