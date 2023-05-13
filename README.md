q# CEOS 17기 백엔드 스터디

## [2주차 미션] 에브리타임 기능 구현하기

### 1. 기능
  - 카테고리별 게시판에서 게시글을 작성, 조회할 수 있음
  - 게시글에 댓글 및 대댓글을 작성할 수 있음
  - 유저별로 학기에 맞는 시간표를 작성할 수 있고 강의에 리뷰를 남길 수 있음
  - 한 명의 유저가 지금까지 수강한 모든 강의들을 조회할 수 있음
  - 동일한 과목도 분반별로 강의목록에 추가할 수 있음
  - 유저간 친구 맺기를 통해 서로의 시간표를 조회할 수 있음

<img width="1076" alt="스크린샷 2023-04-01 오후 8 30 59" src="https://user-images.githubusercontent.com/98458302/229289722-bbc8d75d-7bfa-4605-8ec8-585ef7a25737.png">

<br></br>

### 2. 모델
  - 유저: User
  - 커뮤니티: Board, Post, Comment, Reply
  - 시간표: Timetable, Course, CourseInfo,Friend_list, Review

<br></br>

### 3. 미션

<img width="1389" alt="스크린샷 2023-04-01 오후 9 20 16" src="https://user-images.githubusercontent.com/98458302/229290357-cce82734-7829-4c9f-bc5f-244f1062fa5f.png">

#### (1) 데이터베이스에 해당 모델 객체 3개 이상 넣기: 
user 와 course 를 ForeignKey로 연결하여 timetable 객체 4개 생성
#### (2) 삽입한 객체들을 쿼리셋으로 조회하기:
`Timetable.objects.all()` 로 만들어진 Timetable 객체들을 조회
#### (3) filter 함수 사용해보기:
`Timetable.objects.filter(user__username=”ImTakGyun”)`로 유저의 timetable을 조회

### 4. 겪은 오류와 해결 과정
#### (1) AbstractUser을 활용하여 User Model 확장시, 확장전에 migrate을 통해 기본 제공 User Model이 생성되어 버린 문제
  - 이미 생성된 기본 User Model 삭제하기
    - 생성되어 있는 회원과 관련된 앱의 migrations폴더에서 __pycache__폴더와 __init__.py를 제외하고 다 지워주기
    - DB에서 살려야할 데이터를 백업해 주신 다음 과감하게 DROP
    - 백업한 데이터를 새 DB에 넣어주기
    - (현재 상황에서는 데이터를 넣기 전이라서 백업은 진행하지 않았다. 나중에 추가로 공부할 예정!)

#### (2) 같은 테이블에서의 서로 다른 레코드를 외래키로 가져올 때의 충돌 오류 -> 'Django: reverse accessors for foreign keys clashing'
  - models.ForeignKey(User, related_name='##')
    - 충돌하는 두 키를 related_name 을 통해 각각 명시함으로써 해결

#### (3) User Model을 AbstractUser을 활용하여 확장 후 기본 User Model을 명시해주지 않아 발생한 오류 
####   -> Reverse accessor for 'api.User.groups' clashes with reverse accessor for 'auth.User.groups'
####   -> Reverse accessor for 'api.User.user_permissions' clashes with reverse accessor for 'auth.User..user_permissions'
  - setting.py 에 AUTH_USER_MODEL = 'api.User' 를 명시함으로써 해결

### 5. 회고
  - 에브리타임 기능을 구현하기 위해 ERD 설계에 많은 시간을 쏟았다.
  - 커뮤니티의 경우 이전에 고민한 적이 있어서 고민이 없었지만, 의외의 복병은 시간표였다.
  - 같은 강좌도 분반마다 Course 테이블에 추가하면 되겠거니 생각했었는데 그렇게 되면 강의평이 분반마다 생성되기에 
  - Course_Info 테이블을 추가로 생성함으로써 같은 강좌의 강의평은 한번에 조회가 가능하도록 조회했다.
  - 또 요일마다 다른 강의실을 쓰는 강의의 경우 요일과 교시 그리고 강의실 3가지를 고려해야했는데
  - 요일/교시 테이블과 강의실 테이블 그리고 강의정보를 조합하며 하나의 강의를 만들게 되면 조회시에 join 연산도 많아질 뿐만 아니라
  - 하나의 강의 정보를 조회할 때 여러개의 레코드를 프론트에 반환해주며 프론트에서 이를 통합해서 나타내야하기에 번거롭다는 생각이 들었다.
<img width="379" alt="스크린샷 2023-04-01 오후 10 55 08" src="https://user-images.githubusercontent.com/98458302/229293346-2e13f428-0b5f-4bb7-8720-ed79a1b95023.png">



  - 때문에 강의계획서를 바탕으로 요일/교시 와 강의실을 문자열로 받아 split 을 통해 구분지어줌을 가정으로 설계하였지만
  - 분명 보다 좋은 설계 기법이 있을 것 같다...(계속 고민해봐야지...)
  - Django가 아직 낯설기는 하지만 확실히 편리한 기능도 많고 알아가는 맛이 있다.
  - 설게 고민에 시간을 쏟느라 기능 대한 이해가 부족하여 코드를 엉망진창으로 짯지만 그래도 고생했다...ㅎㅎ
  - 열심히 공부해서 클린하게 만들어 나가야지

<br></br>

## [3주차 미션] API 만들기
### 0. DRF(Django REST Framework) 사용하기
- **pip install djangorestframework** 를 통해 DRF 설치하기
- **settings.py**의 **INSTALLED_APPS**에 **rest_framework** 추가하기

### 1. CBV 로 API 만들기
- **모든 데이터를 가져오기**
- **URL** :`community/post/`
- **Method** : `GET`

<pre><code>
[
    {
        "id": 1,
        "created_at": "2023-04-08T05:16:49.897442",
        "updated_at": "2023-04-08T05:16:49.897498",
        "title": "제목은 제목",
        "content": "내용은 내용",
        "image1": null,
        "image2": null,
        "image3": null,
        "user": 2,
        "board": 1
    },
    {
        "id": 2,
        "created_at": "2023-04-08T18:34:35.832509",
        "updated_at": "2023-04-08T18:34:35.832583",
        "title": "제목은 제목이지 내용이겠냐",
        "content": "내용은 내용이지 제목이곘냐",
        "image1": null,
        "image2": null,
        "image3": null,
        "user": 1,
        "board": 1
    }
]
</code></pre>
<img width="1024" alt="스크린샷 2023-04-08 오후 6 37 43" src="https://user-images.githubusercontent.com/98458302/230726178-7eca4d66-6d8a-45b5-af65-d8736e2cbf98.png">

- **특정 데이터 가져오기**
- **URL** : `community/post/2/`
- **Method**: `GET`

<pre><code>
{
			"id": 2,
      "created_at": "2023-04-08T18:34:35.832509",
      "updated_at": "2023-04-08T18:34:35.832583",
      "title": "제목은 제목이지 내용이겠냐",
      "content": "내용은 내용이지 제목이곘냐",
      "image1": null,
      "image2": null,
      "image3": null,
      "user": 1,
      "board": 1
}
</code></pre>

<img width="1024" alt="스크린샷 2023-04-08 오후 6 47 37" src="https://user-images.githubusercontent.com/98458302/230726367-3bcab978-afad-45f2-9181-8da2dbcfd8bf.png">

- **새로운 데이터 생성하기**
- **URL** : `community/post/`
- **Method**: `POST`
- **Body** : `{"title": "제목은 제목인데 내용일수도?", 
              "content": "내용은 내용인데 제목일수도?",
              "user": 2, 
              "board": 2}`

<pre><code>
{
    "id": 4,
    "comment": [],
    "text": "새로운 post",
    "likes_count": 0,
    "created_at": "2020-04-14T17:23:32.572431+09:00",
    "updated_at": "2020-04-14T17:23:32.572431+09:00"
}
</code></pre>

<img width="1014" alt="스크린샷 2023-04-08 오후 6 46 36" src="https://user-images.githubusercontent.com/98458302/230726527-95b0816c-d23f-4180-850c-4e514b1f5bab.png">

- **특정 데이터 삭제하기**
- **URL** : `community/post/1`
- **Method**: `DELETE`

<img width="1024" alt="스크린샷 2023-04-08 오후 6 51 19" src="https://user-images.githubusercontent.com/98458302/230726672-f5484230-ea2d-4561-a268-c39b5f9c4eb2.png">

- **특정 데이터 업데이트하기**
- **URL** : `community/post/3`
- **Method**: `PUT`
- **Body** : `{"title": "제목은 제목이지 내용은 아니지", 
               "content": "내용도 내용이지 제목은 아니지",
               "user": 2, 
               "board": 2}`

<pre><code>
{
    "id": 3,
    "created_at": "2023-04-08T18:46:27.291140",
    "updated_at": "2023-04-08T19:46:59.245255",
    "title": "제목은 제목이지 내용은 아니지",
    "content": "내용도 내용이지 제목은 아니지",
    "image1": null,
    "image2": null,
    "image3": null,
    "user": 2,
    "board": 2
}
</code></pre>

<img width="1006" alt="스크린샷 2023-04-08 오후 7 47 14" src="https://user-images.githubusercontent.com/98458302/230726784-1a47e67c-9b08-429e-813e-4344762418c8.png">

### 2. Viewset으로 리팩토링하기
- 기존의 CBV 형태로 작성한 코드를 모두 주석으로 처리해주고 Viewset 형식으로 바꿔준다.

#### community/urls.py

<pre><code>
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('post', PostViewSet)

urlpatterns = router.urls
</code></pre>

#### community/views.py

<pre><code>
from rest_framework import viewsets
from .serializers import *

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
</code></pre>

- 그 많던 코드가 달랑 위의 5줄로 바뀌는 매쥑이 일어났다.
- ModelViewset의 정말 편리한 점은 기본적으로 Retrieve, List, Create, Destroy, Update의 뷰를 제공한다는 것이다.
- 또한 Router에서 제공하는 router.register( ) 기능을 통해 경로와 특정 Viewset을 매핑시켜줌으로써
- API 접근시 **Http Method**와 경로 마지막의 **<int:pk>/** 유무를 통해 특정 Viewset에서의 요청을 알아서 처리해준다.

### 3. Filter 기능 구현하기
#### Setting
- **pip install django-filter** 명령어를 통해 django-filter를 설치하기
- **settings.py**의 **INSTALLED_APPS**에 **django-filter** 추가하기
- 물론 filter를 직접적으로 사용하여 해당 Viewset에서 filtering 기능을 이용할 수 있겠지만
- 파일 이름에 따라 가독성을 주기위해 views.py에는 뷰만이 존재해야한다고 판단하여 filter.py 파일을 생성하여 필터들을 분리해주었다.

#### community/filters.py

<pre><code>
from django_filters.rest_framework import FilterSet, filters
from .models import *

class PostFilter(FilterSet):

    title = filters.CharFilter(lookup_expr='icontains', field_name='title')
    user = filters.NumberFilter(field_name='user_id')
    board = filters.NumberFilter(field_name='board_id')

    class Meta:
        model = Post
        fields = ['title', 'user', 'board']
	
</code></pre>
- 뷰에 연결하고자 하는 Filter를 설정하는 단계이다.
- 게시글의 경우 제목을 통한 검색이 이루어지는데 검색어가 포함되어 있는 게시글을 모두 출력해야하기에
- 필터링 설정에서 **lookup_expr** 을 **icontains** 로 설정해줌으로써 대소문자 구분없이 검색어가 포함된 모든 게시글이 출력되게 하였다.
- (혹시 대소문자를 구분하며 정확한 문자열의 비교를 원한다면 해당 설정을 **exact**로 바꿔주면 된다.)
- 필터에 설정된 Meta class 에서는 어느 모델을 이용할 것이고 해당 모델의 어떤 필드값으로 필터링을 할 것인지 명시해준다.

#### community/views.py

<pre><code>
...

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
</code></pre>
- 해당 뷰에서 어떤 필터를 사용할 것인지 명시해준다.

#### TEST
<img width="1024" alt="스크린샷 2023-04-08 오후 10 49 57" src="https://user-images.githubusercontent.com/98458302/230729442-545c5940-687e-4f4d-b60d-d88fca267bdf.png">
<img width="1024" alt="스크린샷 2023-04-08 오후 10 54 11" src="https://user-images.githubusercontent.com/98458302/230729446-1119b983-3f92-491c-9c45-b70177b9466f.png">


### 4. 회고
- 확실히 Django에는 편리한 기능이 너무나도 많은 것 같다.
- Viewset과 같이 기본적으로 제공해주는 것들이 정말 많아서 개발자 입장에서 구현하는 시간이 확실히 단축될 것 같다.
- 다만 세부적인 커스터마이징이 필요할 경우 해당 기능들을 제공해주는 라이브러리의 내부 구조에 대한 확실한 이해가 필요할 것 같다.
- 이번 과제의 경우 뷰를 만들고 해당 뷰에서의 요청 처리와 데이터 반환에 관한 복잡하지 않은 내용이었기에
- 별다른 오류없이 수월하게 진행되어 열 받을 일이 없어 다행이었다.
- 이번 미션을 수행하며 장고의 동작 방식에 대한 이해에 굉장히 도움이 된 것 같고 재미있었다.
- 이제 시험공부 열심히 하다가 또 돌아와야지
- 모두들 시험 잘보고 다시 만납시다. 화이팅~

<br></br>

## [4주차 미션] DRF2 - Simple JWT
### 1.로그인 인증
- 필요성: HTTP 통신으로 요청하면 응답이 한 후 종료되는 stateless 특징때문에 연결이 끊어어지므로 누가 로그인 중인지를 기억해야 하기 때문

### 1.1 세션과 쿠키를 이용한 인증
- 사용자의 계정 정보를 읽어 사용자를 인증한 후, 고유한 ID를 발급하여 세션에 저장해두고 세션 ID를 가지고 통신하는 방법으로
- 서버는 HTTP 응답 헤더에 발급된 Session ID를 실어 보내면서 사용자의 브라우저에서 쿠키를 생성하게(Set Cookie) 하고
- 사용자의 브라우저는 이후 매 요청마다 HTTP 요청 헤더에 Session ID가 담긴 쿠키를 실어서 보낸다.
- 서버는 HTTP 요청 헤더에 존재하는 쿠키를 열어 Session ID를 확인하고 세션 저장소에서의 대조를 통해 사용자를 인증 후 데이터를 응답해준다.

### 장점
- 사용자의 정보는 세션 저장소에 저장되고, 발급된 Session ID 를 통해 통신하기 때문에 Session ID가 담긴 쿠기가 통신 도중 노출되더라도 유의미한 값을 갖고있지 않아서 안전하다.
- 각각의 사용자는 고유의 Session ID를 발급 받기 때문에 일일이 회원 정보를 확인할 필요가 없어 서버 자원에 접근하기 용이하다.

### 단점
- 하이재킹 공격(쿠키를 탈취하여 사용자인척 요청을 보내는 접근 공격)의 가능성 <br/>
-> HTTPS 프로토콜 사용과 세션에 만료 시간을 넣어주는 것으로써 해결.
- 세션 저장소를 사용하기 때문에 추가적인 저장공간이 필요하다.

<br></br>

### 1.2 Json Web Token을 이용한 인증
- 사용자를 인증하고 식별하기 위한 정보들을 암호화시킨 토큰을 통해 사용자의 인증, 인가를 진행하는 방식이다.
- **Token** = Header + Payload + Verify Signature
- **Header** <br/>
-> 토큰의 타입(**typ**)과 암호화할 방식(**alg**)을 설정
- **Payload** <br/>
-> 토큰에 담을 정보를 포함
-> 보통 만료 일시, 발급 일시, 발급자, 권한정보 등을 포함
-> 클레임(정보의 일부)의 종류로는 Registered, Public, Private로 3가지가 존재
- **Verify Signature** <br/>
-> Payload가 위변조되지 않았다는 사실을 증명하는 문자열(JSON의 변조를 체크)
-> Base64 방식으로 인코딩한 Header, Payload 그리고 SECRET KEY로 더한 후 Header에서 설정한 암호화 함수로 암호화한 서명값

- 사용자의 로그인 요청을 통해 서버는 계정 정보를 읽어 사용자를 확인 후, 사용자의 고유한 ID값을 부여하고 Payload에 정보를 넣어 Token을 생성한다.
- 생성된 Access Token을 HTTP 응답 헤더에 실어 사용자에게 보냄으로써 사용자는 인증이 필요한 요청마다 토큰을 HTTP 요청 헤더에 실어 보내고
- 서버에서는 해당 토큰의 Verify Signature를 SECRET KEY로 복호화한 후, 조작 여부, 유효 기간을 확인하고 Payload를 복호화하여 사용자에 맞는 데이터를 응답해준다.

### 장점
- JWT는 발급 후 검증만 거치면 되기 때문에 추가적인 저장공간이 필요없다.
- 확장성이 뛰어나다.(토큰 기반으로 하는 다른 인증 시스템에 접근이 가능)

### 단점
- 한 번 발급되면 유효기간이 완료될 때까지는 계속 사용이 가능하며 중간에 삭제가 불가능하다.
- 따라서 해커에 의해 정보가 노출된다면 대처할 방법이 필요하다.
-> Access Token의 만료 시간을 짧게 잡고 Access Token의 재발급을 요청하는 Refresh Token을 추가적으로 발급하여 해결.
- Payload 정보가 디코딩하면 누구나 접근할 수 있기에 중요한 정보들을 보관할 수 없다.
- JWT의 길이가 길기 때문에, 인증 요청이 많아지면 서버의 자원낭비가 발생한다.

<br></br>

### 1.3 OAuth 2.0 을 이용한 인증
- 별도의 회원가입 없이 외부 서비스에서도 인증을 가능하게 하고 해당 서비스의 API를 이용하게 해주는 프로토콜
- Resource Owner(사용자)가 Client(웹 어플리케이션)에게 인증 요청을 하게되면
- Client는 Authorization Request(인증 요청)를 통해 Authorization Server(인증 서버)에게 로그인 페이지를 요청하고 Resource Owner에게 보내준다.
- Resource Owner가 인증을 완료하면 Authorization code가 발급되고 url에 실어 Client에게 보내준다.
- Client는 해당 코드를 Authorization Server에 보냄으로써 유저 정보와 Access Token, Refresh Token을 받급받는다.
- Client는 해당 Access Token을 DB에 저장하거나 Resource Owner에게 넘겨주고
- Resource Owner가 Resource Server의 자원이 필요하면, Client는 Access Token을 담아 Resource Server에 요청하여 자원을 이용한다.
- 만일 Access Token이 유효하지 않다면, Client는 Authorization Server에 Refresh Token을 보내 Access Token을 재발급 받아 Resource Server에 자원을 요청한다.
- 만일 Refresh token이 유효하지 않다면, Resource Owner는 새로운 Authorization Grant를 통해 발급받은 코드를 Client에게 넘겨준다.

<br></br>

### 2. JWT 로그인 구현하기
- 우선, 기존의 AbstractUser를 상속받아 진행했던 UserModel을 사용편의성을 위해 AbstractBaseUser를 상속받는 것으로 변경했다.

### 2.1 Simple-JWT 설치하기
<pre><code>
pip install djangorestframework-simplejwt
</code></pre>

<pre><code>
# settings.py

# 기본 유저모델 설정
AUTH_USER_MODEL = 'account.User'

INSTALLED_APPS = [
	...
    # simple-jwt 추가
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}

# JWT_AUTH 설정
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': env('JWT_SECRET_KEY'),
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
</code></pre>

- SIMPLE_JWT 내에서는 JWT와 관련된 설정들을 정의해준다.
- 일단 레퍼런스를 참조하여 가져왔기 때문에 추후에 좀 더 깊게 공부하며 각각의 설정들이 무슨 역할을 하는 것인지 확인해볼 예정이다.
- 우선 주의깊게 보아야할 설정들은
- **'ACCESS_TOKEN_LIFETIME'** : access token이 유효한 기간
- **'REFRESH_TOKEN_LIFETIME'** : refresh token이 유효한 기간
- **'ROTATE_REFRESH_TOKENS'** : refresh token이 오면 새로운 access token과 함께 refresh token 또한 새로 반환해줄지
- **'ALGORITHM'** : 사용할 암호화 기법
- **'SIGNING_KEY'** : 서명키(토큰 생성에 사용할 비밀키)
- **'AUTH_HEADER_TYPES'** : JWT 인증 타입

<br></br>

### 2.2 회원가입 구현하기
- 회원가입 API를 통해 POST 요청, 데이터가 잘 채워져있다면 Serializer를 통해 저장하고 저장된 데이터를 응답해준다.
<img width="986" alt="스크린샷 2023-05-06 오전 4 08 24" src="https://user-images.githubusercontent.com/98458302/236616367-bc66e8a3-1261-4ef5-9e52-ce667d954903.png">

<br></br>

### 2.3 로그인 구현하기
- Login_id와 Password를 가지고 POST 요청을 통해 로그인을 진행한다.
- 'django.contrib.auth'의 authenticate 함수를 통해 유효한 회원임을 확인 후, 토큰을 발급해준다.
- 발급된 토큰을 그대로 HTTP 응답 헤더에 실어 보내도 되지만,
- 한 번 생성한 토큰은 삭제가 불가능하다는 문제로 인해 로그아웃 기능 구현을 위해 쿠키를 사용하기로 했다.
- set_cookie 라는 명령을 통해 응답으로 보내준 토큰들을 브라우저가 cookie를 형성하여 그 속에 갖고 있도록하였다.
- 자세한 내용은 로그아웃 부분에서 이어서 설명하겠다.
- 정상적으로 로그인 작동함을 확인했다.
<img width="996" alt="스크린샷 2023-05-06 오전 4 08 36" src="https://user-images.githubusercontent.com/98458302/236617126-68c15169-25ca-4be6-a914-e10f41a25ac7.png"> <br/>
- Cookie 또한 형성되어 토큰을 지니고 있다.
<img width="1018" alt="스크린샷 2023-05-06 오후 4 59 07" src="https://user-images.githubusercontent.com/98458302/236617176-1a47319e-221a-4206-bed1-65fa40adcd2a.png"> <br/>
- 잘못된 계정으로 로그인을 진행하면 에러 메세지가 출력된다.
<img width="1009" alt="스크린샷 2023-05-06 오전 4 09 00" src="https://user-images.githubusercontent.com/98458302/236617285-1e5342c2-beb9-411c-ae76-904ce3a566ba.png">

<br></br>

### 2.4 Refresh Token으로 Access Token 재발급 받기
- SIMPLE_JWT에 내장된 기능으로 구현하였다.
- 재발급을 받기 위한 경로를 추가적으로 정의해줬다.
- Refresh Token을 가지고 POST 요청을 보내주면 새로운 Access Token이 발급되어 응답되는 식으로 진행된다.
<pre><code>
# urls.py

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), #회원가입하기
    path("auth/", AuthView.as_view()), #로그인하기
    path('auth/refresh/', TokenRefreshView.as_view()),#토큰 재발급하기
]
</code></pre>
<img width="1017" alt="스크린샷 2023-05-06 오후 5 01 37" src="https://user-images.githubusercontent.com/98458302/236617822-7fcf6b8d-331d-4f0e-a253-c14a9aecbee8.png">

<br></br>

### 2.5 로그아웃 구현하기
- 이전 ios 프로젝트에서는 앱 개발이었기 때문에 쿠키를 사용할 수 없어 토큰의 수명을 짧게 잡고 구현하였다.
- 때문에 로그아웃의 경우 그저 화면상에서만 로그아웃을 진행시켜주었고 토큰을 살려두는 식이었다.
- 하지만 웹의 경우 브라우저에서 만드는 쿠키가 사용가능하므로 쿠키에 토큰을 저장하고 로그아웃 요청이 오면 쿠키를 삭제시키는 명령을 통해 사용자에게서 토큰을 삭제시킬 수 있었다.
- 물론 토큰 그 자체가 사라진 것이 아니고 사용자에게서 빼앗은 수준이므로 크게 변하는 것은 없다...(해커에게 노출되면 큰일나는 것은 똑같다...)
- 그저 새로운 방식으로 로그아웃을 구현함에 흥미를 느껴 쿠키를 이용하는 것이다.

- 정상적으로 로그아웃이 진행되었다는 응답과 함께 쿠키에서 토큰이 사라진다.
<img width="1016" alt="스크린샷 2023-05-06 오후 4 58 41" src="https://user-images.githubusercontent.com/98458302/236617857-4dfafc81-ef3a-4886-a4c2-7b5cec9a0d8e.png">
<img width="1015" alt="스크린샷 2023-05-06 오후 4 59 32" src="https://user-images.githubusercontent.com/98458302/236617871-f2a7b480-4500-4469-898b-ced980f9639a.png">

<br></br>

### 3. 겪은 오류와 해결
- (1) AbstractBaseUser의 고유식별자를 명시하지 않아 발생한 오류
- AbstractUser에서 AbstractBaseUser를 상속받는 것으로 코드를 고치고 migrate를 진행하였더니 다음과 같은 오류가 발생했다.
<img width="621" alt="스크린샷 2023-05-06 오전 2 33 46" src="https://user-images.githubusercontent.com/98458302/236617985-935274c7-f221-4c3c-be7a-029fde26920e.png"> <br/>
- AbstractUser는 AbstractBaseUser와 다르게 이미 고유식별자가 포함되어 있어서 USERNAME FIELD를 사용할 필요가 없지만
- AbstractBaseUser에서는 USERNAME FIELD = '고유식별이 될 컬럼' 을 통해 고유식별이 가능하게 설정을 해주어야 한다고 한다.
- 따라서 USERNAME_FIELD = 'login_id' 를 Model 구현부분에 삽입해줌으로써 해결하였다.

<br></br>

- (2) 사용자 정의 모델에 대한 사용자 관리자를 생성해주지 않아서 발생한 오류
- Postman을 통해 로그인을 Test하는 도중 갑자기 서버가 다운되는 에러가 발생하였다.
<img width="585" alt="스크린샷 2023-05-06 오전 4 02 45" src="https://user-images.githubusercontent.com/98458302/236618570-5994238f-546f-43d9-9842-d5b981d207b9.png"> <br/>
- 오류가 발생한 원인은 관리자가 생성되어 있지 않다는 것이었다.
<img width="660" alt="스크린샷 2023-05-06 오전 4 02 10" src="https://user-images.githubusercontent.com/98458302/236618585-da60c522-112c-4050-9be8-6d3d8065a61a.png"> <br/>
- 사용자 정의 모델을 사용하는 경우 사용자 관리자인 UserManager()을 설정해줘야했다.
- UserModel의 구현부에 objects = UserManager() 를 삽입해줌으로써 해결하였다.

<br></br>

### 4. 회고
- 확실히 로그인과 회원가입에 관해서는 레퍼런스들이 차고 넘친다.
- 몇가지 레퍼런스를 대조해보며 이해하고, 또 따라서 구현하였더니 큰 어려움이 없었다.
- 또 이전 프로젝트에서 스프링부트 시큐리티를 공부하며 진행했던 내용이라서 더 그랬던 것 같다.
- Django에서는 Simple-JWT를 통해 보다 빠르고 간단하게 구현이 가능했던 것 같다.
- 이제 시험도 끝났고 팀도 정해졌고... 화이팅이다...!!!! 힘내자!
