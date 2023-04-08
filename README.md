# CEOS 17기 백엔드 스터디

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

### 1. Viewset으로 리팩토링하기
- 기존의 CBV 형태로 작성한 코드를 모두 주석으로 처리해주고 Viewset 형식으로 바꿔준다.

####community/urls.py

<pre><code>
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('post', PostViewSet)

urlpatterns = router.urls
</code></pre>

####community/views.py

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


