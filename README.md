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
 
 # CEOS 17기 백엔드 스터디

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

