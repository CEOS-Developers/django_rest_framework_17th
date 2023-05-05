# CEOS 17기 백엔드 스터디

## 서비스 요구사항

이번 과제로 작성한 프로그램의 요구사항은 크게 학교기능 ,유저기능, 게시판 그리고 시간표 기능으로 나뉜다.
이후에 각 가능은 다음과 같은 기능을 구현해야한다.

### 전체 기능

* 학교를 구분할 수 있어야 한다.
* 학과를 구분할 수 있어야 한다.

### 유저 기능

* 회원가입
* 별명 설정
* 친구 추가
* 가입일자

### 게시판

* 글 쓰기
* 댓글 쓰기
* 대댓글 기능
* 익명 기능
* 질문글 기능
* 댓글 수정 기능
* 댓글 삭제 기능
* 댓글 읽기 기능
* 글 종아요 기능
* 글 신고 기능
* 글 스크랩 기능
* 댓글 좋아요 기능
* 댓글 신고 기능

### 시간표

* 시간표 추가 기능
* 시간표 공개 여부
* 시간표 과목 추가
* 과목 별점
* 과목 교수 조회

## ERD 모델

이 과제의 ERD 모델은 다음과 같다.

![ETD_TABLE](./image/erd_table.png)

## ORM 사용

![ORM](./image/ORM.png)

ORM 명령어로 3개의 학교를 넣은 뒤 objects.all 명령어를 사용해서 학교를 전부 조회하였다.

이후에 objects.filter를 사용해서 sogang이라는 이름을 가진 학교를 조회한다.

## 과제를 하면서 알게된 정보와 오류 수정과정

### User

* 처음에는 너무 귀찮아서 AbstractUser를 상속받아서 원래 상속된 필드를 그대로 받는 방식으로 하였다.
* 하지만 지원이가 User기능을 구현하려는 것을 보고 이대로 살면 안되겠다는 생각과 함께 결국 AbstractUser가 아닌 AbstractBaseUser를 상속받아서 유저를 구현하는 것으로 방식을 전환하였다.
* 솔직히 구현하는데 좀 짜증나긴했음
* 구조는 다음과 같다.

~~~python
class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
~~~

으로 2개의 class를 상속 받은 이후에
objects 변수에 UserManger를 실행해서 object를 초기화를 한다.

UserManager를 구현하는 방식은 다음과 같다.

~~~python

class UserManager(BaseUserManager):

    def create_user(self, username, password, nickname, **extra_fields):
        pass

    def create_superuser(self, username, password, nickname=None):
        pass
~~~

create_user 함수와 create_superuser함수를 구현해서 일반 유저 생성과 superuser생성하는 함수를 구현한다.

이후에는 자신이 원하는 필드를 추가하면 완성!

마지막으로 manage.py에서
AUTH_USER_MODEL 를 설정하고 자신의 user class의 위치를 가리키면 앱에서 돌아갈 준비가 완료된 것이다.

### 기타

* migration을 할 때는 app마다 migration을 진행해야 한다.
* 솔직히 migration 잘못해서 골치가 아픈 경우가 많고, 개발 단계이므로

~~~shell
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
pip install --upgrade --force-reinstall Django
~~~

를 입력한 이후에 mysql 로 들어가서 프로젝트를 위한 테이블을 찾은 이후에

~~~mysql
DROP DATABASE (데이터베이스 이름)
CREATE DATABASE (데이터베이스 이름)
~~~

을 해주면 충돌 없이 수정 사항을 다시 적용할 수 있다.

역시 밀어버리는 방식이 너무 속 편하다.

* 그래도 미는 것이 별로 좋은 방법은 아니므로 makemigration을 그냥 치는거보다는 make migrations (앱 이름)을 해주도록 하자
* ID 필드를 설정할 때는 일반 primary key 보다는 UUID를 활용하는 것이 좋다. [링크](https://stir.tistory.com/294) 모든 기술에는 장점과 단점이 있으니 잘 판단해서 사용하자
* 클래스 내에 Meta 라는 클래스를 선언하여 모델의 기타 작동 방식을 정의 할 수 있다.
* global_entity/models에서 BaseEntity를 선언하여서 Meta값에 abstract=True라고 해서 상속 가능하게 클래스를 변경하였다.
* edittable=False로 진행하면 django 페이지에서 값을 주지 못한다.
* 장고에서 객체의 primary키 이름은 설정하지 않는다면 클래스 이름을 모두 소문자로 나타낸 값이다.
* 하지만 나중에 외래키를 사용하는 과정에서 이름 충돌이 나기 시작하고 db이름을 쓰는 convention에 따라서 primary key값을 클래스이름_id와 같은 방식으로 선언하였다.
* primary_key를 설정할 때는 AutoField를 이용해서 설정해준다.

## 회고

* erd 테이블을 짤 때 상당히 고전했고, 유저를 만드는 과정에서 상당히 고생하였다.
* 이번에 기능을 완성할 때 마다 readme를 작성하지 않아서 문제가 생긴 부분이 어디인지 잘 기억이 나지 않았다.
* 다음에는 기록 잘하자!

## step CBV

![사진](./image/results.png)

이와 같이 모든 정보를 가져오는 api 를 구현하였다.

또한 모든 정보를 가져오는 url 이외에도 pk를 통해서 특정 정보를 가져오는 api, 특정 정보를 삭제하는 api, 특정 정보를 수정하는 api를 구현하였다.

~~~python
urlpatterns = [
    path('', views.AllBoardView.as_view(), name='all_board'),
    path('<int:pk>/', views.OneBoardView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
~~~

## step ViewSet

![사진](./image/fail.png)

그러나 viewSet으로 수정했을 때는 끝내 실패했다.
왜 이런지는 모르겠지만, 다른 사람들의 실습을 보면서 참고를 할 예정이다.

추정되는 이유로는

~~~python
filter_backends = [DjangoFilterBackend]
filterset_class = BoardFilter
~~~
를 설정했는데 여기에서 BoardFilter 클래스로 정상적으로 입력이 가지 않는 것이 원인인것 같다.

## 알게 된 점

* 장고 adminpage에서 유저 정보를 저장할 때는 password encrypt가 발생하지 않는다.
* as_view 메서드는 해당 클래스가 모든 것을 알아서 하게 놔둔다는 의미를 지닌다.
* ModelViewSet 은 ixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
  mixins.ListModelMixin, GenericViewSet 를 상속한다. 이상적인 것은 get, post, put 연산에 따라서 상속을 받는 방법이 제일 이상적이다.
* delete 연산을 할 때는 perform_destroy 메서드를 오버라이딩해서 delete 연산을 커스터마이징이 가능하다.
* filterset_class는 filter를 해주는 class이고, filterset_fields는 filter를 해주는 field이다. 후자가 훨씬 구현에서는 이득을 가진다.
* filter는 주로 문자 이외에 모든 것을 다루고, search는 주로 문자를 다룬다.
* viewSet은 미스터리인거 같다.

# 추가적인 JWT_AUTH 설정
~~~PYTHON
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
    'USER_ID_FIELD': 'username',
    'USER_ID_CLAIM': 'username',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
~~~

* 여기에서 user_id_field 에서 USER_ID_FIELD, 디비에서 보는 부분이고, USER_ID_CLAIM 은 토큰에 필드로 넣어주는 부분이다.

~~~python
user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
~~~

* 요청에서 받아온 body에 있는 username과 password를 받아서 authenticate 함수에 넣어준다. 로그인이 완료되면 user라는 객체를 반환한다.

## Q1 로그인 인증은 어떻게 하나요? & Q2 JWT는 무엇인가요?

로그인은 크게 2가지 개념으로 구성 되어있다.

1. 인증(Authentication)
    * 사용자가 누구인지 확인하는 절차
2. 인가(Authorization)
    * 사용자를 식별하고 인증된 사용자에게만 권한을 부여하는 절차
    * 자원의 접근에 대한 허가라고 생각하면 된다.

이런 로그인 과정을 매번 사용자가 접속할 때 마다 수행하는 것은 매번 암호화 연산을 수행하는 만큼 비효율적이다.
그래서 세션과 쿠키와 같은 방법을 사용해서 

* 쿠키 & 세션
    쿠키는 클라이언트(브라우저) 로컬에 저장되는 작은 데이터 파일을 말하고, 세션은 세션ID를 통해서 로그인 되어있음을 지속하는 상태를 말한다. 
    인증된 사용자의 식별자와 랜덤한 문자열로 세션 ID를 만들어서 서버에 저장하고 응답헤더에 넘겨서 클라이언트가 저장할 수 있게 한다. 그리고 쿠키에 저장을 하고 있다가 다음 로그인  때 해당 세션 id를 넘긴다.

* JWT
    하지만 세션은 서버의 database를 조회하는 방식으로 서버에 무리를 줄 수 있어서 상태가 존재하지 않는 JWT 토큰을 사용한다.
    이 때 토큰이 탈취 당하게 된다면, 악의적인 사용자에 의해서 지속적으로 사용당할 수 있으므로, 토큰의 유효기간을 짧게 설정해야 한다.
