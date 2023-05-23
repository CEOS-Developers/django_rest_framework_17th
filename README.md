# CEOS 17기 백엔드 스터디

## 구현 기능
   : 1) boards : 글쓰기, 클릭한 게시물 보기, 모든 게시물 보기  
     2) accounts : 로그인, 로그아웃, 회원가입  
     3) comments : 게시글에 댓글 달기  
     4) tags : 태그 기능은 게시글을 작성할때 그글이 포함되어 있는 내용을 단어로 요약한것입니다. 게시글을 작성할때마다 개수의 제한 없이 태그를 입력받을수 있고 입력받은 값을 저장하되 기존에 겹치는 태그는 늘리지 저장이아닌 불러오는 형식으로 구현했습니다.  
     5) timetables :시간표 만들기(강의 등록 등), 친구맺기, 과목 등록하기  참고 링크 : https://ssungkang.tistory.com/entry/Django-10-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EB%A1%9C%EA%B7%B8%EC%9D%B8%EB%A1%9C%EA%B7%B8%EC%95%84%EC%9B%83-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
   
## 겪은 오류와 해결 과정  
![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c3bab068-f117-4477-bacb-2d8bbb08c19c/Untitled.png)  
 -> 연동 완료!
  1) error code 1046 : No database selected : **use [schema 이름];** 을 빼먹었다 ;; 즉 어떤 스키마에 데이터베이스를 설치할 지 정해주며 테이블 생성을 시작해야한다.  
  2) error code 1824 : Failed to open the referenced table ‘board’ : article table을 만들려다가 오류가 났다. 이유는 데이터베이스들은 ‘관계형’이다. 따라서 생성되는 순서가 중요하다. board가 있어야 article이 존재할 수 있다. 생성 순서 중요   
  3) error code 1072 : column을 먼저 추가한 후 key 값으로 설정할 수 있음. 이거 안해서 계속 에러 뜸..    
  4) error code 1681 : mysql이 더 이상 int에 length를 정하는 것을 지원하지 않는다. 따라서 int 옆에 적어준 길이를 지정하지 않았더니 해결됐다.  
  참고 링크 : https://nayha.tistory.com/230
  5) RuntimeError : Model class boards.models.Board doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS   
    이런 류의 에러가 자꾸만 떠서 고생을 많이 했다… ㅠ 이때는
    ![Untitled (2)](https://user-images.githubusercontent.com/90204371/230026935-8f77d3ff-5bfb-46c2-be7a-09f10ccd2888.png)
    [settings.py](http://settings.py) 나 이번 과제의 경우 [base.py](http://base.py) 에 들어가면서 INSTALLED_APPS 에 내가 빠뜨린 앱이 없는지 살펴보면 된다.  
  6) page not found 오류 : runserver를 했지만 페이지가 안떴다. 이 때 path('',home)을 해주니 로그인 해주세요! 라는 문구가 뜨면서 해결이 됐다.  

## 새롭게 배운 점  
  1) .env 파일은 보안을 유지하기 위해 설정하는 파일로 dev.py를 바꾸면 안된다고 한다…  
  2) 자동증가 : 스키마를 작성하다보면 데이터의 수를 p.k로 설정해야 할때가 있다. 이럴경우 새로 데이터를 insert할때마다 max(num)으로 기존에 추가되어있는 num의 최대값을 알아야 p.k값이 겹치지 않게 추가를 할 수있다. 하지만 *insert마다 이렇게 num의 최대값을 받아오는 sql문을 작성하는것은 비효율적*이므로 num에 Auto_Increment 속성으로 insert문을 보낼때 마다 자동으로 num값이 증가되게 저장할 수 있다.  
  3) ERD 추출하기 : MySQL 이 알아서 추출해준다 !_! 완전 신기하다 (feat. 재령)  
  ![Untitled](https://user-images.githubusercontent.com/90204371/230025525-69fbb8b6-e13f-42d5-8198-25e8ccbba560.png)
  ![Untitled (1)](https://user-images.githubusercontent.com/90204371/230026295-dcfd4fe6-405d-4b19-bea6-9840010159b1.png)
그래서 다음과 같이 테이블을 형성해보았다.
참고링크 : https://bamdule.tistory.com/44

  4)  
   python [manage.py](http://manage.py/) makemigrations accounts  
   python [manage.py](http://manage.py/) migrate accounts  
   python [manage.py](http://manage.py/) migrate  

  1번의 경우, accounts/models.py에 저장한 모델을 등록전 테이블 양식을 생성해주는것이다.  
  2번의 경우, 생성해준 테이블양식을 적용하는 절차이다.  
  3번의 경우, 앱의 모델이 아닌 전에 설정한 settings.py와 그 외의 데이터베이스에 들어갈 변경사항을 적용시키는 절차이다.  

## 궁금한 점

## 느낀 점  
  : 다른 일정과 몸살이 겹쳐서 과제를 시간 안에 완벽하게 완수하지 못한 게 아쉽지만 그래도 끝까지 포기 안하고 대부분의 모델링은 구현해서 다행이라고 생각했습니다. 그리고 예시를 통해 저번 과제를 좀 더 실질적으로 이해할 수 있어서 유익했습니다 :)

## 회고  
 좀 더 자세한 과정 및 회고는 노션 링크로 달아두었습니다.  
 https://thin-pangolin-e02.notion.site/Django-2-0412d38d89ca40e6ace5c91621d5c819
 
 ## 5주차 미션
## 참고 사이트
https://inma.tistory.com/88

## 모든 데이터를 가져오는 api 만들기
# error 1) AttributeError: module ‘.views’ has no attribute CommentList
![Untitled (3)](https://user-images.githubusercontent.com/90204371/230721440-e80f2ec0-45ee-43b6-a0e0-9b2d6fc57323.png)
path 명을 제대로 적어주지 않아서 문제가 생긴 것이었다.
https://forum.djangoproject.com/t/django-attributeerror-module-views-has-no-attribute/17241

# error 2) django.db.migrations.exceptions.NodeNotFoundError: Migration 
![Untitled (4)](https://user-images.githubusercontent.com/90204371/230721439-17a6119f-6bd4-42da-9f57-672d1756eea3.png)

migration 에러가 도대체 몇번이나 난건지 ㅠㅅㅠ

그때마다 각 앱에 있는 migration 파일들을 아예 지우고 다시 makemigrations → migrate 를 해줬다. 기존에 migration 파일이 있으면 안되는 것이다. 정현이가 조언해준 덕분에 해결할 수 있었다.
> I had the same problem. It is because of the inconsistent migration history. So I deleted the migrations directory in all installed apps and then called `python manage.py makemigrations` command. The new migrations had no problem.
> 

심지어는 mysql에 있는 eveyrtime 테이블을 아예 지워버리기도 했다. (feat. 현우오빠)

# error 3) django migrate gets error "table already exists"
https://antilibrary.org/911
이 또한 migrations 에러였는데 

> python [manage.py](http://manage.py) migrate —fake <appname>
> 

으로 마치 마이그레이션이 완료된 것처럼 해준다.

# error 4) 404 error
![Untitled (5)](https://user-images.githubusercontent.com/90204371/230721437-cca17258-aa72-48f0-8206-67a34383ccea.png)

아무리 코드를 살펴봐도 잘못된 게 없는데 postman에서 404 에러가 발생했다. 알고보니 url뒤에 enter가 아스키코드 값으로 인식되어 에러가 난 것이었다.. 탁균오빠와 상훈이랑 도합 4시간은 삽질한 것 같다.

오류를 고친 이후에는 아래와 같이 결과가 잘 나타났다.
![Untitled (9)](https://user-images.githubusercontent.com/90204371/230721430-fa5658d9-424b-4b90-97ce-755bcf3a172e.png)
![Untitled (8)](https://user-images.githubusercontent.com/90204371/230721434-788dd9c9-425a-40ab-b5ee-33204d0a6b6e.png)
![Untitled (7)](https://user-images.githubusercontent.com/90204371/230721435-caf504c2-7748-4cc2-8eb0-b5c4d9266b57.png)
![Untitled (6)](https://user-images.githubusercontent.com/90204371/230721436-f9611ca7-2b87-41a3-9101-0ed69cb48c9e.png)

# viewset & filterset
1) viewset 이란?    
- mixins 와 viewsets를 상속받아서 적용  
- 함수를 따로 만들지 않아도 get post 등의 함수가 구현되어 있음
- Mixins 란 : 특정한 클래스에 상속을 통해 기능을 추가하는 것.  
class PostViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):  
    serializer_class = PostSerializer  
    queryset = Post.objects.all()  
    
2) FilterSet 이란?   
> filtering 작업( queryset에서 특정 queryset을 고르는 작업 ) 을 손쉽게 사용하도록 DRF(Django REST Framework)에서 제공하는 속성.  
클라이언트가 접근하는 API url에 붙은 query parameter을 자동으로 필터의 옵션으로 인식하고 필터링을 함.  
>
FilterSet 사용 방법  

- class Meta :  
    - filterable한 모델 정의  
    - 사용할 필드 정의  
    - Disable fields : exclude  
    - Ordering : order_by  
    - Group fields : together 
    
import django_filters  

class PostFilter(django_filters.FilterSet):  
    class Meta:  
        model = Post  
        fields = ['author', 'content', 'upload_date']  
        order_by = ['upload_date']  

## 회고
하면 할 수록 백엔드 flow에 대한 이해도가 높아지는 것 같아서 뿌듯하다. 그리고 회고 쓰는 skill도 향상된 것 같다. 좀 더 가독성있게 쓸 수 있게 되었다.  

그리고 저번에도 띄어쓰기를 해서 인식이 안되는 문제가 있었고 이번에도 enter가 아스키 코드로 해석돼서 안되는 문제가 있었다. 형식 실수를 하면 안되겠구나 하는 걸 뼈저리게 느꼈다 ㅎ 그리고 postman도 파이참 터미널을 보고 에러를 잡아낼 수 있다는 것을 알게 되었다.  
-----------------------------------------------------------------------------------------------------------------------------
## 5주차 미션
## 노션 링크
https://www.notion.so/DRF2-Simple-JWT-Permission-1859a7fc0ae54905ac86558d06403755?pvs=4

##이론
# Q1. 로그인 인증은 어떻게 하나요?
# A.
# 세션 - 쿠키
![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b94289ca-6f80-467f-a105-3abfd506d847/Untitled.png)
세션-쿠키 방식

⇒ 세션-쿠키 방식이란 웹에서 활용하는 로그인 보안 방식으로 로그인 요청을 보내게되면 서버 측에서는 세션에서 세션ID를 생성하여 Response의 Header에 존재하는 SetCookie 옵션에 담아 클라이언트에게 전달하게된다.

응답을 받은 클라이언트는 Response의 SetCookie 옵션에의해 웹 브라우저단에서 Cookie를 생성하게되고

이 Cookie에는 서버에서 전달받은 세션ID가 담겨 이후 클라이언트의 요청시 Header에 담겨 서버에 전달되게 된다.

**문제점) 보안이 굉장히 취약하다는 점이다.**

공격자의 공격에 의해 Cookie에 담긴 세션ID가 노출되게 되면 해당 공격자는 이 세션ID를 가지고 **이용자 행세를 하며** 공격이 가능해지기 때문이다.

이를 막기 위한 방법으로는 세션에서 세션ID를 생성할 때 유효기간을 쥐어주면 되는데 이렇게 되면 보안적인 부분은 향상될 지 몰라도 세션ID의 유효기간이 지나게되면 사용자를 로그아웃 시켜 재로그인하게 만드는 로직을 추가해야하고 사용자의 편의성도 떨어지는 문제가 발생한다.

또한 많은 이용자가 존재하는 서비스에서 세션-쿠키 방식은 메모리를 굉장히 많이 차지하게 되고 이를 해결하기 위해서는 레디스 라는 DB를 이용해야되기에 비용이 굉장히 많이 들게 된다. (일반적인 DB는 접근 속도가 느려 로그인과 같이 빠른 처리를 위한 로직에 적합하지 않다)

이러한 보안 취약성과 편의성을 해결하고자 등장하게 된 것이 JWT 방식으로 앱에서 사용되는 로그인 보안 방식이다.

# Q2. JWT 는 무엇인가요?
# A.
# JWT(JSON Web Token)
- 당사자 간에 정보를 JSON 형태로 안전하게 전송하기 위한 토큰(서버와의 통신에서 권한 인가에 사용)  
- URL에서 사용할 수 있는 문자열로만 구성되어 있어 HTTP 구성요소 어디든 위치 가능  
- 구성: <Header>.<Payload>.<Signature>  
- <Header> : alg(해싱 알고리즘 - SHA256), typ(토큰의 타입 - JWT)로 구성  
    - 완성된 헤더는 Base64Url 형식으로 인코딩되어 사용된다.  
- <Payload> : 정보  
    - Registered Claims(필수는 아닌 이름이 지정되어 있는 클레임들) :  
        - iss : JWT의 발급자 주체, 대소문자를 구분하는 문자열  
        - sub : JWT의 제목  
        - aud : JWT의 수신인, JWT를 처리하려는 주체는 해당 값으로 자신을 식별해야 함 (요청 처리의 주체가 aud 값으로 자신을 식별하지 않으면 JWT는 거부됨)  
        - exp : JWT의 만료시간 설정(NumericDate 형식)  
        - nbf : Not Before을 의미  
        - iat : JWT가 발급된 시간  
        - jti : JWT의 식별자 값 (JWT ID), 중복 처리를 방지하기 위해 사용  
    - Public Claims : 키와 값을 마음대로 정의 가능(But 충돌이 발생하지 않을 이름으로 설정)  
    - Private Claims : 통신 간에 상호 합의되고 등록된 클레임과 공개된 클레임이 아닌 클레임  
    - JWT 예시:  
        {
	    "sub" : "wikibooks payloda",
	    "exp" : "1602603401",
	    "userId" : "wikibooks",
	    "username" : "flature"
        }
        - 이렇게 완성된 내용은 Base64Url 형식으로 인코딩되어 사용된다.
- <Signature> : <Header>.<Payload>를 비밀키와 함께 헤더에 정의된 암호화 함수로 암호화한 부분  

JWT 방식으로 앱에서 사용되는 로그인 보안 방식이다.  

JWT 방식의 경우 이용자가 로그인을 하게되면 서버에서는 이용자의 식별자를 담은 짧은 유효기간을 갖는 액세스 토큰과 비교적 긴 유효기간을 갖는 리프레쉬 토큰을 만들어 클라이언트에 반환해주고 클라이언트는 리프레쉬 토큰을 저장해두고 앞으로의 요청에서는 액세스 토큰을 요청의 헤더부에 담아 사용하게 된다.   

만일 액세스 토큰의 유효기간이 지나게 되면 클라이언트는 리프레쉬 토큰을 통해 서버에 새로운 액세스 토큰을 발급 받을 수 있다. 마찬가지로 리프레쉬 토큰의 유효기간이 지나게 되면 새롭게 리프레쉬 토큰을 요청하거나 사용자를 로그아웃 시켜 재로그인을 하게 만들 수 있다.   

이러한 JWT 방식은 액세스 토큰을 탈취당하여도 짧은 유효시간으로 공격 가능 기간을 최대한 단축시키고 혹여나 리프레쉬 토큰을 탈취 당하여도 유효한 액세스 토큰이 존재시에 재발급이 불가능하게 막는 로직 등을 통해 보안성이 높고 리프레쉬 토큰을 통해 세션-쿠키 와는 달리 잦은 사용자의 재로그인을 할 필요가 없어져 사용자의 편의성 측면에서도 효과적이다.  

특히 토큰 내부에 사용자 식별을 위한 값이 암호화 된 상태로 존재하기에 세션이 필요없어지고 이로인해 메모리 공간의 여유와 레디스를 사용해야하는 비용적인 측면을 해결해준다.  

> 주요 개선점 3가지  
1. 보안성을 높여줌  
2. 잦은 재로그인을 막아 편의성을 높여줌  
3. 메모리 아낄 수 있고 비용을 절감해줌  
>

# +) JWT와 simple JWT의 차이 :  
JWT는 JSON Web Token의 약자로, 웹 애플리케이션에서 사용자 인증 정보를 안전하게 전송하기 위한 토큰 기반 인증 방식입니다. JWT는 페이로드에 사용자 정보를 넣고 서명하여 안전한 토큰을 생성하며, 이를 서버와 클라이언트 간에 주고받아 인증을 수행합니다.  

Simple JWT는 JWT를 구현하기 위한 파이썬 라이브러리 중 하나입니다. Simple JWT는 JWT를 쉽게 생성하고 검증할 수 있는 다양한 기능을 제공합니다. 이 라이브러리를 사용하면, Django 및 Django REST Framework에서 JWT를 사용하여 웹 애플리케이션을 보다 쉽게 개발할 수 있습니다. 

따라서, Simple JWT는 JWT를 더 쉽게 사용할 수 있도록 도와주는 라이브러리이며, JWT는 웹 애플리케이션에서 사용자 인증 정보를 안전하게 전송하기 위한 토큰 기반 인증 방식입니다.  

# +) Csrf 토큰  
- Cross Site Request Forgery  
- csrf 공격은 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위를 특정 웹사이트에 요청하게 하는 공격을 말한다.  
- `CsrfViewMiddleware`는 Django의 `MIDDLEWARE` 설정에서 기본적으로 활성화 되어있다.  

[https://docs.djangoproject.com/en/4.2/ref/csrf/](https://docs.djangoproject.com/en/4.2/ref/csrf/)  

[https://chagokx2.tistory.com/49](https://chagokx2.tistory.com/49)  

##구현
*serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#User = get_user_model()
fields = '__all__'
class RefreshToken(RefreshToken):
    def for_user(cls, user):
        token = super().for_user(user)
        return token

class LoginSerializer(serializers.Serializer):
 id = serializers.CharField(write_only=True, required=True)
 password = serializers.CharField(write_only=True, required=True)

 def validate(self, request, username=None):
     id = request.get('id', None)
     password = request.get('password', None)

     if User.objects.filter(username=id).exists():
         user = User.objects.get(username=id)
        if not user.check_password(password):
             raise serializers.ValidationError({"Wrong Password"})
        else:
         raise serializers.ValidationError({"User doesn't exist."})

     token = RefreshToken().for_user(user)
     refresh = str(token)
     access = str(token.access_token)

     data = {
         'id': user.id,
         'id': user.username,
         'refresh': refresh,
         'access': access
     }
     
*views.py     
class Login(APIView):

    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))

        if user is not None:
            token = TokenObtainPairSerializer.get_token(user)
            access_token = token.access_token
            res = Response(
                {
                    "message": "login success",
                    "token": str(token.access_token)
                },
                status=status.HTTP_200_OK,
            )

            res.set_cookie("access", access_token, httponly=True)
            return res
        else:
            return HttpResponse("target failed")
	    
     # models.py
  class User(AbstractBaseUser, PermissionsMixin):
      objects = UserManager()

      id = models.CharField(primary_key=True, max_length=17, verbose_name="id", unique=True)
      username = models.CharField(max_length=17, verbose_name="아이디", unique=True)
      nickname = models.CharField(max_length=100, verbose_name="이름", null=True)
      date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일', null=True, blank=True)

      is_active = models.BooleanField(default=True)
      is_staff = models.BooleanField(default=False)
      is_superuser = models.BooleanField(default=False)

      USERNAME_FIELD = 'username'
      REQUIRED_FIELDS = []


      def __str__(self):
          return self.username 
	    
        
## 결과
1) SUCCESS
![image](https://user-images.githubusercontent.com/90204371/236601208-b5099d3e-6703-4254-a130-1ce0845a627d.png)


2) ERROR : ID가 존재하지 않을 때
![image](https://user-images.githubusercontent.com/90204371/236530836-6a7d5183-47cd-4313-8baf-f845de91d087.png)
 

## 오류 해결
![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e1225ab8-d25f-430c-b886-9b7f34739db7/Untitled.png)  
계속 404 Not Found 오류가 뜨는 것이었다. 403 Forbidden도 떴었다.  
그 이유는  
url에 로그인 기능을 구현하는 함수의 path를 적어주지 않아서 그런 것이었다.

또한 mysql로 수동으로 데이터값을 넣어준 이후에도 계속 bad request가 떴었는데  
그 이유는 mysql에서 넣은 데이터와 장고가 문자열 타입이 맞지 않아서였다.

→ register class를 등록해 회원가입을 구현했다.

<배운 점>  
- CBV 적는 방법 : views.Login.as_view()  
- path를 적어주어야 함수를 사용할 수 있다. 빼먹지 말자.  
    - 대소문자 주의!

###6주차 과제
# AWS : https 인증  

저번 과제와 관련이 없는 줄 알았지만 ec2에서 탄력적 ip를 할당해야해서 아니었다. 그래서 5주차 과제를 참고하여 탄력적 ip를 할당해보자.    

1) 인스턴스 생성     
![Untitled (10)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/a64eddef-0b0f-4d89-aa94-c228ec773d92)  
![Untitled (11)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/6d5252ae-1198-4ce9-a02d-173eb80401f6)  
![Untitled (12)](https://github.com/doleebest/dj  
![Untitled (13)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/7ab7867b-dea4-4fc3-9389-e1085096a039)
![Untitled (14)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/c56dc858-4b87-4bb5-8960-06314b3d2f93)

2) 이렇게 생성한 퍼블릭 ip 주소를 입력해주었다.   

#**1️⃣ AWS의 Route 53에서 원하는 도메인을 구입한다.**  

가비아에서 도메인을 구매한 후 아래 링크를 참고했다.
	https://developer-ping9.tistory.com/320
가비아 설정을 다 했다.  
![Untitled (15)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/00e6ecf6-1930-440e-bd81-4dfdfbc67f0e)
ae89a3e9a138)
	![Untitled (13)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/7ab7867b-dea4-4fc3-9389-e1085096a039)
![Untitled (14)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/c56dc858-4b87-4bb5-8960-06314b3d2f93)
![Untitled (15)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/00e6ecf6-1930-440e-bd81-4dfdfbc67f0e)

# **2️⃣ AWS의 Certificate Manager에서 원하는 도메인에 대한 SSL 인증서를 받는다.**  
![Untitled (16)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/3d351a59-dd99-4899-9cb7-4bf5d150f7bb)
에러 ) 계속해서 인증서가 발급이 안돼서.. 밤을 샜는데 가비아 홈페이지에 있는 “aws certification manager에 있는 주소”를 복붙해서 네임서버 주소에 넣었어야하는데 그렇지 않아서 발급이 안되는 것이었다.  

다행히 발급이 되었다..  
https://www.youtube.com/watch?v=gK7xnCqCucY  

# **3️⃣ 서버로 사용할 Ec2 인스턴스에 대해서 Elastic Load Balancer(로드밸런서)를 등록한다.**  

~~노션 설명을 보니 ALB를 쓴 것 같아서 ALB로 설정하고 그것이 뭔지 더 조사해보았다.~~ 아닌 것 같다 ㅋ  그럼 왜 이름이 ALB인거지
### Application Load Balancer (ALB)  

- 7계층, 즉 HTTP 전용 로드 밸런서로 머신 간 다수 HTTP 어플리케이션의 라우팅에 사용된다.  
    
    그래서 HTTP/HTTPS 트래픽을 처리하는 로드밸런싱에 최적화 되어 있다.  
    
- 이러한 머신들은 대상 그룹이라는 그룹으로 묶이게 됨.  
    
    동일 EC2 인스턴스 상의 여러 Applicaion에 부하를 분산하고 컨테이너와 ECS를 사용하게 된다.  
    
- HTTP/2와 WebSocket을 지원하며 Redirect도 지원하므로,  
    
    HTTP에서 HTTPS로 트래픽을 자동 Redirect하려는 경우, 로드 밸런서 레벨에서 가능하다는 의미가 됨. 그러므로 기존의 CLB 보다 많은 장점을 포함하고 있다.  
    
- ALB는 Path-based routiong (경로 라우팅)을 지원하여 ALB에 연결된 인스턴스들은 여러개의 URL과 path를 가질 수 있다.  

쭉쭉 설정을 하고 가장 중요한 부분은 **Listeners and routing !**  
![Untitled (17)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/f24db30a-64d3-4c0a-8f28-98f58e509b92)

리스너를 등록하고, 해당 포트로 들어오는 요청을 타겟그룹으로 넘겨주게 된다. 이전에 만들어둔 타겟 그룹을 사용하면 된다.  
	
$4️⃣ 80번 포트로 들어오는 요청은 Redirect, 443번 포트로 들어오는 요청을 인스턴스로 연결해준다.  
리디렉션 대상을 재설정해주었다.
![Untitled (20)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/7de03dae-819d-4a50-a8b9-a56a3c0b6672)

nginx 리다이렉션 로직 추가 (선택적)

```bash
if ($http_x_forwarded_proto != 'https') {
return 301 https://$host$request_uri;
}
```
	
#5️⃣ 등록한 로드밸런서를 AWS Route 53의 도메인의 레코드에 등록한다.  
![Untitled (21)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/edb1a2c0-2948-44e3-8c65-ae89a3e9a138)


#6️⃣ ec2 인바운드 규칙 443 추가  
https://dbjh.tistory.com/65

HTTPS 설정 후, 테스트 API 만들어서 Postman을 통해 배포된 EC2 DNS 주소로 요청해보기    
![Untitled (22)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/3f705508-b7dc-416b-865c-827bcd9a7150)
![Untitled (23)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/1a02dfd4-23dc-4b8a-b956-96ca1400606a)
ango_rest_framework_17th/assets/90204371/5994542d-b752-4625-a0f3-7b0eb2410e07)

	
'''
(myenv) C:\Users\이소정>pip install django
Collecting django
  Using cached Django-4.2.1-py3-none-any.whl (8.0 MB)
Collecting asgiref<4,>=3.6.0
  Using cached asgiref-3.6.0-py3-none-any.whl (23 kB)
Collecting tzdata; sys_platform == "win32"
  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Collecting sqlparse>=0.3.1
  Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Installing collected packages: asgiref, tzdata, sqlparse, django
Successfully installed asgiref-3.6.0 django-4.2.1 sqlparse-0.4.4 tzdata-2023.3
WARNING: You are using pip version 20.2.3; however, version 23.1.2 is available.
You should consider upgrading via the 'c:\users\이소정\myenv\scripts\python.exe -m pip install --upgrade pip' command.

(myenv) C:\Users\이소정>pip install --upgrade pip
Collecting pip
  Using cached pip-23.1.2-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.2.3
    Uninstalling pip-20.2.3:
      Successfully uninstalled pip-20.2.3
ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: 'C:\\Users\\이소정\\AppData\\Local\\Temp\\pip-uninstall-z74mi9zt\\pip.exe'
Consider using the `--user` option or check the permissions.


(myenv) C:\Users\이소정>django-admin startproject myproject

(myenv) C:\Users\이소정>cd myproject

(myenv) C:\Users\이소정\myproject>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 20, 2023 - 22:34:08
Django version 4.2.1, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[20/May/2023 22:34:21] "GET / HTTP/1.1" 200 10731
[20/May/2023 22:34:22] "GET /static/admin/css/fonts.css HTTP/1.1" 404 1816
Not Found: /favicon.ico
[20/May/2023 22:34:22] "GET /favicon.ico HTTP/1.1" 404 2113



Microsoft Windows [Version 10.0.19045.2965]
(c) Microsoft Corporation. All rights reserved.

C:\Users\이소정>pip install django djangorestframework
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: django in c:\users\이소정\appdata\roaming\python\python39\site-packages (3.2.16)
Requirement already satisfied: djangorestframework in c:\users\이소정\appdata\roaming\python\python39\site-packages (3.14.0)
Requirement already satisfied: asgiref<4,>=3.3.2 in c:\users\이소정\appdata\roaming\python\python39\site-packages (from django) (3.6.0)
Requirement already satisfied: pytz in c:\users\이소정\appdata\roaming\python\python39\site-packages (from django) (2021.1)
Requirement already satisfied: sqlparse>=0.2.2 in c:\users\ 이소정\appdata\roaming\python\python39\site-packages (from django) (0.4.3)


C:\Users\이소정>cd myproject

C:\Users\이소정\myproject>python manage.py startapp myapp

C:\Users\이소정\myproject>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 20, 2023 - 23:12:18
Django version 3.2.16, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
'''
![Untitled (25)](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/f5a07bf4-b12b-4f13-8b21-e7900e00c092)
	![image](https://github.com/doleebest/django_rest_framework_17th/assets/90204371/f116b298-2a13-4a87-ab7d-729aef288903)

	
## 질문)
ALB가 아닌 instance를 사용했던데, 왜 target group 이름은 ceos-ALB-targetgroup인지?  
## 회고)
중간에 인증서 발급이 안되어서 애먹고 밤을 쌩으로 샜지만..  
그래도 평소에 내가 매일매일 쓰는 http 주소의 작동원리를 알 수 있어서 의미있었다.
https://purring-backbone-cc0.notion.site/AWS-https-790fd3e2e893413494c4280daf774d65
