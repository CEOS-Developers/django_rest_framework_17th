# CEOS 17기 백엔드 스터디  

## [2주차]  

### ORM 이용해보기  
1. 게시글 생성  
![image](https://user-images.githubusercontent.com/90256209/229326431-a573d2b4-03b6-4c8c-a2bf-7e14ad507831.png)
2. 게시글 수정 및 쿼리셋 조회  
![image](https://user-images.githubusercontent.com/90256209/229326491-4cb57511-12ba-45a1-9274-ba3bde83da88.png)
3. filter 함수 사용  
filter의 `__contains`와 `__startswith`을 사용해봤다.
![image](https://user-images.githubusercontent.com/90256209/229326506-cf1c83a1-0b5c-43bd-bda9-5308a030df27.png)

---
### ERD 설계  
실무에서 ERD를 그린 후에 SQL문을 export해서 DB에 넣는 경우, ERD에 관계선으로 연관관계(Ex 1:N)를 설정해두면 테스트 데이터를 넣기가 불편해서 거의 하지 않는다고 배워서 습관적으로 관계선 설정을 안했더니 테이블간 관계가 한눈에 안들어오는것 같다  

![CEOS  everytime](https://user-images.githubusercontent.com/90256209/229327752-7a75378c-b28a-4298-96c8-baa159f407f6.png)
ERD를 설계하기전에 연관관계 매핑에 대해 생각해봤다.  
- User1과 User2의 관계 : User1은 여러명의 유저와 친구가 될 수 있고, User2도 여러명의 유저와 친구가 될 수 있으므로 다대다(N:M) 관계임 -> 중간 테이블 'Friend'로 관리  
- Board(게시판), Post(게시글), Comment(댓글)의 관계 : 각 게시판에 여러개의 글이 있고, 각 글은 하나의 게시판에 소속되므로 게시판과 게시글은 1:N 관계임. 각 게시글에 여러개의 댓글이 있을 수 있고, 각 댓글은 하나의 게시글에 소속되므로 게시글과 댓글도 1:N 관계  
- User가 Post/Comment를 작성하는 관계 : 유저는 여러개의 게시글/댓글을 쓸 수 있고, 각 게시글/댓글은 한명의 유저에 의해 쓰였으로 유저가 게시글/댓글을 작성하는 관계는 1:N 관계  
- User가 Post를 Likes(공감)과 Scrap(스크랩)하는 관계 : 유저는 여러개의 게시글을 공감/스크랩할 수 있고, 각 게시글은 여러명의 유저에 의해 공감/ 스크랩될 수 있으므로 다대다(N:M) 관계임 -> 중간 테이블 'Likes', 'Scrap'으로 관리  
- Photo(사진)와 Post의 관계: 각 게시글에 여러 사진을 올릴 수 있으므로 1:N
- TimeTable(시간표), Lecture(강의)의 관계: 각 시간표에 여러 강의를 추가할 수 있고, 각 강의도 여러 시간표에 포함될 수 있으므로 N:M -> 중간 테이블 'TakeLecture(수강)'로 관리
- LectureReview(강의평)와 Lecture의 관계: 각 강의에 여러 강의평이 달릴 수 있고, 각 강의평은 하나의 강의에 소속되므로 1:N 관계  

그리고 고민됐던건 시간표에 강의를 추가할때 '일반교양' > '16이후, 공학' > '인문계열' 이런식으로 전공/영역을 선택하면 강의가 여러개 나오는 부분이었다. 이렇게 전공/영역이 계층구조를 가지기 때문에 LectureDomain(전공/영역) 테이블을 따로 추가했다.  
예를들어,  
![image](https://user-images.githubusercontent.com/90256209/229328515-3fa2a18f-efb0-4c1c-b6b3-b38727d8a8a1.png)  
'한국근현대사' 강의가 lectureDomain_id로 3을 가지면, 인문계열 강의라는 뜻이고, parent_id를 통해 거슬러 올라갈 수 있다!  
parent_id의 default는 0으로 최상위 영역이다.  
강의 시간에 대해서도 고민이 됐는데 강의 테이블에 string으로 넣었다.

---  
### 겪은 오류와 해결 과정
처음에 model을 작성할때 굳이 역참조 안해도 되는 테이블들에 related_name을 다 넣었더니 Reverse accessor for ~ clashes with reverse accessor for ~ 에러가 났다. 구글링해보니 related_name이 필수인 경우는 한 테이블(클래스)에서 서로 다른 두 컬럼(필드)이 같은 테이블(클래스)을 참조하는 경우뿐이어서 나의 경우에는 해당되지 않아 삭제했다.

오류는 안났지만 User를 OneToOne 방식으로 확장할때 User에서 email, password, username과 같은 필드를 기본 제공해준다는걸 까먹고 Profile에 중복되는 필드를 넣어서 나중에 삭제했다.

---
### 새롭게 배운 점  
ManyToMany(다대다)관계를 설정하는 방법에 대해 알게되었다. 다대다 관계에서 중간테이블을 만든다는건 알고있었지만 Django에서 어떻게 모델링하는지(through를 통해서)는 처음 알게됐다. through는 반드시 다대다 관계중에서 한곳에만 선언해야 한다.  다대다 관련해서는 더 공부해야겠다,,
[참고1](https://velog.io/@jiffydev/Django-9.-ManyToManyField-1) [참고2](https://hoorooroob.tistory.com/entry/%ED%95%B4%EC%84%A4%EA%B3%BC-%ED%95%A8%EA%BB%98-%EC%9D%BD%EB%8A%94-Django-%EB%AC%B8%EC%84%9C-Models-%EB%8B%A4%EB%8C%80%EB%8B%A4-%EA%B4%80%EA%B3%84%EC%97%90%EC%84%9C%EC%9D%98-%EC%B6%94%EA%B0%80-%ED%95%84%EB%93%9C)  

---
### 느낀점  
장고를 쓰다보니 편한점들이 보이는것 같다. 일단 admin.py 기능은 최고야,, User 클래스에서 이미 많은 필드가 정의되어있는것도 신기했다.  
ERD 설계는 언제해도 고민되는 부분이 많은것 같다. 하다보니까 진짜 에브리타임 DB는 어떻게 되어있을지 궁금해졌다. 테이블이 엄청엄청 많겠지?  
모델을 분리했어야 하는데 이번 과제는 다른일들때문에 너무 늦게시작해서 아쉬움이 남는다 담부턴 더 미리 시작하자  

---
## [3주차]  

### API 명세
우선적으로 어떤 CBV API를 만들지 에브리타임을 구경하면서 리스트업해봤다
![image](https://user-images.githubusercontent.com/90256209/231825029-5d62ead3-c302-45c6-82ed-8cea6ec22733.png)  
게시글 삭제 및 수정 API에 대해 말을 하자면, 원래 DELETE 는 사용을 지양해야 한다고 들은지라… (사실 손사래 치시면서 절대 쓰지 말라고 하셨따 하하) 항상 PATCH 로 모델의 status 를 ‘D’로 바꾸는 식으로 개발했었는데 장고에서는 아무리 구글링해봐도 views.py 에서 수정을 이런식으로 구현한게 없더라 그래서 partial 을 활용해서 PUT 으로 status 필드만 수정할 수 있도록 구현했다(그냥 PUT 은 모든 필드를 다 채워서 요청해야해서 불편하니까) 찾아보니까 장고에서는 소프트 딜리트를 하기 위해서 SoftDelete 모델을 구현하는 것 같더라. 어쩐지! 나중에 시간 나면 해봐야겠다  

---
### 과제 진행 과정  
1.  패키지 수정  
    
    이전에 api 앱 속 [models.py](http://models.py) 안에 모든 모델이 있던 구조를 여러개의 앱으로 분리했다.  
    
2.  migration 초기화 
    
    모델 구조를 바꿔서 혹시나 하고 migration 파일들을 [init.py](http://init.py) 빼고 다 삭제했더니 아예 데이터베이스 자체가 삭제되서 에러가 나길래 `create database ceosDB;` 로 다시 만들어줬다.
    
3.  account / community / timetable 3개의 앱으로 분리하고, BaseModel 정의를 위한 utils 앱도 만들었다.  
4. API 명세서 작성 - 이번에는 게시글 관련 API들만 만들어봤다.
5. [serializers.py](http://serializers.py) 작성 
    
    게시글(Post)을 가져올때 글쓴이(Profile)의 __PK__, __이름__, __프로필사진URL__ 만 가져오도록 했다. (항상 API의 응답으로 PK는 주는게 좋다, 잊지말자) 
6. [views.py](http://views.py) 및 [urls.py](http://urls.py) 작성
7. 리팩토링 - 피드백 반영 및 Comment 테이블과 LectureDomain 테이블의 parent 컬럼 null 허용  
8. CBV API 작성
9. ViewSet으로 리팩토링 (짱신기)
10. Filter 기능 구현  

---
### 웹 브라우저와 Postman을 통한 API 테스트  

1. 게시글 생성 API (Method: `POST`, URL: `/community/boards/1/`)  
게시판을 지정해서 게시글을 작성해보자  
![image](https://user-images.githubusercontent.com/90256209/231829358-b2af2e20-e2d9-4516-98c6-d8ad87a7ad62.png)  

2. 게시글 수정 및 삭제 API (Method: `PUT`, URL: `/community/posts/1/`)  
partial update로 원래는 `'A'`였던 `status`를 `'D'`로 바꿔줌으로써 게시글을 삭제해보자  
물론 당연히 `title`이나 `contents` 수정도 가능하다  
![image](https://user-images.githubusercontent.com/90256209/231832804-54d1b27c-28b4-4ffe-9acd-1d7c2a573b36.png)  

3. 특정 게시글 조회 API (Method: `GET`, URL: `/community/posts/1/`)  
특정 게시글을 조회해보자  
방금 삭제했기 때문에 `status`가 `'D'`로 바뀐걸 볼수있다  
![image](https://user-images.githubusercontent.com/90256209/231834896-9d1bd72b-97c9-4c21-915c-f6a42942c3de.png)  

4. 전체 게시판 조회 API (Method: `GET`, URL: `/community/boards/`)  
일단은 PK랑 이름만 나오게 했다  
![image](https://user-images.githubusercontent.com/90256209/231837072-5a93ce5f-d33d-44c4-8ec4-2ce1705bb2ad.png)  

5. 특정 게시판 전체 게시글 조회 API (Method: `GET`, URL: `/community/boards/1/`)  
전체 게시글이 조회될때 삭제된 게시글은 보이면 안되니까 `status`가 `'A'`인것만 보이도록 _filter_ 해줬다  
원래는 있었는데요  
![image](https://user-images.githubusercontent.com/90256209/231837919-4b764e4a-5e49-4d6c-84ec-b2025317696f.png)  
삭제하고나면 없어요  
![image](https://user-images.githubusercontent.com/90256209/231838078-43ede8d3-be4b-440f-861f-acc41be05194.png)  

---
### ViewSet으로 리팩토링하기  
요건.. 너무 신기했다 이게 될까? 했는데 진짜 되더랑  
몇줄 안되는 코드로 이렇게 특정 게시글 디테일 보기 및 수정/삭제가 된다  
![image](https://user-images.githubusercontent.com/90256209/231839566-90d6656f-6908-4f44-80c5-c779ddba986e.png)  

---
### Filter 기능 구현하기  
Post가 외래키로 가지는 Board랑 Profile을 서로 다른 방식으로 filter해봤는데 둘다 잘된다.  
Board는  
```
board = filters.NumberFilter(method='filter_board')
# ...
def filter_board(self, queryset, board_id, value):
  return queryset.filter(**{
    board_id: value,
  })
```  
이렇게 메소드로 필터링해봤다.  
Profile은 `profile = filters.NumberFilter(field_name='profile_id')` 이렇게 NumberFilter로 필터링해줬다.  
Title은 `title = filters.CharFilter(field_name='title', lookup_expr='icontains')` 이렇게 'icontains'를 사용해서 검색할 수 있더라  
1. 게시판으로 필터링  
![image](https://user-images.githubusercontent.com/90256209/231843912-bf6032f7-a2bb-4e2a-996d-fd2558233c40.png)  
2. 제목으로 필터링  
![image](https://user-images.githubusercontent.com/90256209/231844302-22024d96-df75-4ac3-bb01-c5ee0eec933f.png)  
3. 글쓴이로 필터링  
![image](https://user-images.githubusercontent.com/90256209/231844565-8c26fa84-7f3f-4c2f-baa4-d96baf1aa42c.png)  

---
### 겪은 오류와 해결 과정  
- 앱을 분리하면서 `Field defines a relation with model 'Profile', which is either not installed, or is abstract` 에러가 나서, `models.ForeignKey("account.Profile", on_delete=models.CASCADE)` 이렇게 외래키에 app이름을 명시함으로써 해결했다.
- API 명세를 고민하다가 Profile 클래스에 `school_id` 를 외래키로 안 넣은걸 발견해서 수정했다. NOT NULL로 설정되어 있다보니 migration할 때 에러가 났는데, 이번만 default를 설정하는 옵션이 있어서 그렇게 해결했다.  
- 이후의 오류와 해결 과정은.. 너무 많은데 머리 싸매느라 못적었다  

---
### 느낀점  
- 장고에서는 어노테이션을 ‘데코레이터’라고 하던데 이름이 뭔가 귀엽다ㅎㅎ  
- 장고는 기본 제공해주는 기능들도 많지만 그만큼 custom할 수 있는 요소도 꽤 많은 것 같아서 생각보다 좋당 근데 구글링을 열심히 해도 자료가 좀 부족한 느낌이 있다ㅠㅠ 장고도 글 많이 써주세요  
- 핫게시판의 기준을 오로지 댓글수+공감수로 한다면 filter 로 구현할 수 있을 것 같다  
- 어짜피 실제로 사용할 만한 세분화된 기능들을 개발하려면 ViewSet안에서도 따로 정의해야할게 많은 것 같은데 이럼 CBV보다 더 좋은건지는 아직 잘 모르겠따  
- 다들 중간고사 잘 마무리하고 만나요👻  

---
## [3주차]  

## 👀 로그인 인증은 어떻게 하나요? JWT 는 무엇인가요?
### 1. Cookie & Session 기반 인증  
- Cookie: 클라이언트가 어떠한 웹사이트를 방문할 경우, 그 사이트가 사용하고 있는 서버를 통해 `클라이언트의 브라우저`에 설치되는 작은 기록 정보 파일  
- Session: 세션은 비밀번호 등 클라이언트의 인증 정보를 쿠키가 아닌 `서버 측에 저장하고 관리`, 브라우저 종료할 때까지 인증상태가 유지됨  
- 동작 방식:  
 1️⃣ 서버는 클라이언트의 로그인 요청에 대한 응답을 작성할 때, 인증 정보는 서버에 저장하고 클라이언트 식별자인 SESSION ID를 쿠키에 담음  
 2️⃣ 이후 클라이언트는 요청을 보낼 때마다, SESSION ID 쿠키를 함께 보냄  
 3️⃣ 서버는 SESSION ID 유효성을 판별해 클라이언트를 식별함  
- 장점: 각 사용자마다 고유한 세션 ID가 발급되기 때문에, 요청이 들어올 때마다 회원정보를 확인할 필요가 없음  
- 단점: 쿠키를 해커가 중간에 탈취하여 클라이언트인척 위장할 수 있는 위험성 존재, 서버에서 세션 저장소를 사용하므로 요청이 많아지면 서버에 부하가 심해짐  

### 2. JWT 기반 인증  
- JWT(JSON Web Token): 인증에 필요한 정보들을 암호화시킨 토큰  
- JWT 구조: `Header` , `Payload` , `Signature` 로 이루어짐. Header는 정보를 암호화할 해싱 알고리즘 및 토큰의 타입을 지정, Payload는 실제 정보(클라이언트의 고유 ID 값 및 유효 기간 등)를 지님, Signature는 인코딩된 Header와 Payload를 더한 뒤 비밀키로 해싱하여 생성 → 토큰의 위변조 여부를 확인하는데 사용됨
- 동작 방식:  
 1️⃣ 클라이언트 로그인 요청이 들어오면, 서버는 검증 후 클라이언트 고유 ID 등의 정보를 Payload에 담음  
 2️⃣ 암호화할 비밀키를 사용해 Access Token(JWT)을 발급함  
 3️⃣ 클라이언트는 전달받은 토큰을 저장해두고, 서버에 요청할 때 마다 토큰을 요청 헤더 Authorization에 포함시켜 함께 전달함  
 4️⃣ 서버는 토큰의 Signature를 비밀키로 복호화한 다음, 위변조 여부 및 유효 기간 등을 확인함  
 5️⃣ 유효한 토큰이라면 요청에 응답함  
 - 장점: 인증 정보에 대한 별도의 저장소가 필요없음, 확장성이 우수함  
 - 단점: 토큰의 길이가 길어, 인증 요청이 많아질수록 네트워크 부하가 심해짐  

### 3. OAuth 2.0을 이용한 인증  
- OAuth: 구글, 페이스북, 트위터와 같은 다양한 플랫폼의 특정한 사용자 데이터에 접근하기 위해 클라이언트(우리의 서비스)가 사용자의 접근 권한을 위임(Delegated Authorization)받을 수 있는 표준 프로토콜.  
쉽게 말하자면, 우리의 서비스가 우리 서비스를 이용하는 유저의 타사 플랫폼 정보에 접근하기 위해서 권한을 타사 플랫폼으로부터 위임 받는 것  
- 나의 앱은 클라이언트👧 / 사용자는 리소스 오너🙋‍♂️ / 구글, 카카오 같은 큰 서비스는 리소스 서버🧝 (사실 데이터 처리를 담당하는 Resource 서버와 인증을 담당하는 Authorization Server로 구성됨)  
- 동작 방식:  
![image](https://user-images.githubusercontent.com/90256209/236613747-47da422f-971f-4d1b-a4c2-2ed0f5dbd972.png)  

---
## 🗣️ 피드백 반영 및 수정사항  
1. 찬혁오빠가 구현한 ***safe delete*** 참고해서 base model에 delete 메소드 추가함  
   데이터 삭제시 deleted_at 컬럼에 삭제시간을 저장하는 방식 = deleted_at이 null이면 정상(=삭제 안된) 게시물  
2. "해당 글의 status는 D인데 조회했을때 보이면 안될 것 같아요🥹🥹"  
   → Filter 클래스에 ***deleted_at이 null인 것만*** 조건을 추가한 ***filter 메소드***를 구현함  

#### (수정한 filter 메소드)  
![image](https://user-images.githubusercontent.com/90256209/236614033-d4ef3388-8987-4dfb-bce0-fcd28f63b5a2.png)  
#### (결과 확인)  
⬇️ 이렇게 DB에서 `deleted_at` 컬럼에 삭제시간이 들어가 있는 경우,  
![image](https://user-images.githubusercontent.com/90256209/236614073-0a8baead-feec-4088-906c-55b99d86fed4.png)  
➡️ postman으로 조회했을때 안보이는걸 확인할 수 있다!! profile_id가 2인 글은 삭제되었으므로 필터링해도 안보임!  
![image](https://user-images.githubusercontent.com/90256209/236614174-b11ebd10-677d-424d-b7d0-5d542ce06e4d.png)  

---
## 👩‍💻 JWT 로그인 구현하기  

### 📌 커스텀 User 모델 사용하기  
`AbstractBaseUser` 를 상속한 커스텀 User 모델을 만들었다. (기존에는 기본 User 모델을 OneToOne 필드로 사용한 Profile 모델을 사용했었음)  
AbstractUser와 AbstractBaseUser의 차이는 기본 제공하는 필드들이 다르다! (AbstractUser가 더 많이 제공함ㅎㅎ)  
+유저 모델을 커스텀할 때
- `USERNAME_FIELD` 은 유저를 고유하게 식별할때 쓰는 필드고,
- `REQUIRED_FIELDS` 는 반드시 필요한 필드다.  
나는 유저 식별을 `email`로 하게끔 만들었다.  
```  
class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=100, unique=True)
    # password, last_login 은 기본 제공
    profile_img_path = models.URLField(blank=True, null=True)
    friends = models.ManyToManyField('self', blank=True)
    school = models.ForeignKey("School", on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    def __str__(self):
        return self.email
```  
UserManager 클래스도 `BaseUserManager`를 상속받아서 커스텀해주었다.

```  
class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, school=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=email,
            nickname=nickname,
            school=school,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, school=None, password=None, **extra_fields):
```  
`create_superuser()`는 `create_user`와 거의 비슷하지만, `superuser.is_admin = True`를 자동 설정한다는 점이 다르다.  


### 📌 회원가입 구현하기  
Postman으로 확인해보니 잘된다ㅎㅎ  
![image](https://user-images.githubusercontent.com/90256209/236615823-7dde4a0b-a8f7-4824-aa42-f054c8362583.png)  
번외) 원래 회원가입할땐 자동로그인이 아니면 토큰 발급을 안한다. 근데 사진에서 쿠키에 뭔가가 있는건 직전에 테스트하던 회원 로그아웃을 안해서 아직 쿠키가 남아있음...ㅎ ~~(NG)~~  


### 📌 JWT Login 구현하기 (Access 토큰, Refresh 토큰 발급)  
로그인 구현할 때 **Access 토큰**은 **HTTP Response**로 프론트한테 주는게 맞는거 같은데, **Refresh 토큰**도 이렇게 줄지 고민이 됐다.  
여러 블로그들을 봤는데, 어떤 사람은 그냥 둘다 Response(JSON 형태)로 주고... 또 어떤 사람은 둘다 쿠키에 넣고... 어떤 사람은 Access 토큰은 Response에, Refresh 토큰은 쿠키에 넣더라ㅎㅎ  
대체 뭐가 더 좋은 방법일까?? 궁금해졌다. 그래서 바아로 구글링했다.  


결론은.. JWT로 보안성이 높은 로그인을 구현하려면,  
⭐**백엔드에서 프론트엔드로 Access Token은 JSON 형태로 넘겨주고, Refresh Token은 Cookie에 넣어주어야 한다**⭐  
아래 링크에 자세한 이유가 나와있다!  
https://medium.com/@uk960214/refresh-token-%EB%8F%84%EC%9E%85%EA%B8%B0-f12-dd79de9fb0f0  


그래서 나도 리프레시 토큰을 쿠키에 넣어주는 코드를 구현했다! (근데 이건 과제니까.. 리프레시 토큰도 JSON 응답에서 한눈에 보고 싶어서 JSON 응답에도 넣어줬다)  


이제, Postman으로 확인해보자!  
- 로그인 성공시 JSON 응답으로 access 토큰, refresh 토큰 둘다 잘 오는걸 확인 가능하다  
![image](https://user-images.githubusercontent.com/90256209/236616656-8ce25ea2-a412-4868-8b48-a951d15c52f2.png)  
- 쿠키에도 refresh 토큰이 잘 들어가 있다  
![image](https://user-images.githubusercontent.com/90256209/236616689-3158903d-eda2-4f05-a272-8c033323d83a.png)  


➡️ 발급 받은 토큰을 디코딩해보면, 유저의 id(pk)와 토큰 발급시간(iat), 토큰 만료시간(exp)을 볼 수 있다.  
내가 `2023-05-06 08:04:08' 에 로그인 했고,  
```  
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
```  
⬇️ 이렇게 토큰 유효기간을 30분으로 설정했기 때문에, 토큰 만료시간은 아래 사진처럼 `2023-05-06 08:34:08` 로 나오는게 맞다!!  
![image](https://user-images.githubusercontent.com/90256209/236616826-4b4bd354-0988-4f1a-be66-ce5841e31122.png)  


### 📌 Refresh 토큰을 통한 Access 토큰 재발급  
로그인할때 access 토큰, refresh 토큰을 발급해주는 걸로 끝내는게 아니라, **실제로 토큰이 만료되었을때 refresh 토큰으로 토큰을 재발급받는 기능**을 구현하고 싶어서 해봤다.  
대략적인 흐름은 `refresh 토큰이 유효한지 확인` → `refresh 토큰에 담긴 유저 id 로 유저 불러오기` → `그 유저로 다시 access 토큰 발급` 이렇다ㅎㅎ  
코드 설명은 주석으로 자세하게 해놓았다..!  
```  
class RefreshAccessToken(APIView):
    def post(self, request):
        # 쿠키에 저장된 refresh 토큰 확인
        refresh_token = request.COOKIES.get('refresh')

        if refresh_token is None:
            return Response({
                "message": "Refresh token does not exist"
            }, status=status.HTTP_403_FORBIDDEN)

        # refresh 토큰 디코딩 진행
        try:
            payload = jwt.decode(
                refresh_token, SECRET_KEY, algorithms=['HS256']
            )
        except:
            # refresh 토큰도 만료된 경우 에러 처리
            return Response({
                "message": "Expired refresh token, please login again"
            }, status=status.HTTP_403_FORBIDDEN)

        # 해당 refresh 토큰을 가진 유저 정보 불러 오기
        user = MyUser.objects.get(id=payload['user_id'])

        if user is None:
            return Response({
                "message": "User not found"
            }, status=status.HTTP_400_BAD_REQUEST)
        if not user.is_active:
            return Response({
                "message": "User is inactive"
            }, status=status.HTTP_400_BAD_REQUEST)

        # access 토큰 재발급 (유효한 refresh 토큰을 가진 경우에만)
        token = TokenObtainPairSerializer.get_token(user)
        access_token = str(token.access_token)

        return Response(
            {
                "message": "New access token",
                "access_token": access_token
            },
            status=status.HTTP_200_OK
        )
```  


➡️포스트맨으로 테스트 해봤더니 새로운 토큰이 잘 발급된다..! 이제 프론트에서는 이 새로운 토큰을 헤더에 넣어서 요청을 보내면 된다.  
![image](https://user-images.githubusercontent.com/90256209/236617483-aabc803a-4800-4e6b-9683-dbd3d9db60eb.png)  


### 📌 JWT Logout 구현하기  
로그아웃 로직은 이렇다.  
1️⃣ 프론트에서 LogoutApi를 호출한다.  
2️⃣ 호출과 동시에 프론트는 가지고 있던 Access token을 삭제한다.  
3️⃣ 백엔드에서는 cookie에 존재하는 Refresh token을 삭제한다.  
그래서 나는 쿠키의 Refresh 토큰을 삭제해주도록 구현했다. Postman으로 확인해보자ㅎㅎ  
![image](https://user-images.githubusercontent.com/90256209/236617700-df7ef90c-afe3-4c40-9541-757e38c4900d.png)  
➡️ 로그아웃이 잘되서 쿠키에 있던 refresh 토큰이 사라진다..!


### 📌 Permission 설정하기  
`permissions.py` 파일을 새로 만들어서 permission을 커스텀해주고, `community` 에 있는 게시판, 게시글 API에 적용해줬다.  
```  
class IsOwnerOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        # 로그인한 사용자인 경우 API 사용 가능
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # GET, OPTION, HEAD 요청일 때는 그냥 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        # DELETE, PATCH 일 때는 현재 사용자와 객체가 참조 중인 사용자가 일치할 때만 허용
        return obj.myUser == request.user
```  
➡️ Postman으로 확인해보자. 게시판 조회 API에 JWT가 잘 적용되었는지 볼 것이다  
- 유효기간이 만료된 경우: 이렇게 친절하게 알려준다ㅎㅎ  
![image](https://user-images.githubusercontent.com/90256209/236618467-ceff90f0-a51a-4207-8db5-be76f02758a2.png)  
- 유효한 토큰으로 다시 요청을 보내면, 다시 잘 보인다!  
![image](https://user-images.githubusercontent.com/90256209/236618489-518bad5d-c67d-4a3f-8552-7d6a0c3c9f7b.png)  

---
## 🍀 느낀점  
***장고는 편리하다...*** 놀랐던게 장고에서는 클라이언트가 넘겨준 JWT로 유저를 불러오는걸 무려 **함수 하나**로 제공한다.. JWT를 추출해서, 파싱하고, 디코딩하고, 유저ID를 추출해서, 그 유저ID로 DB에서 유저 정보를 불러오는 로직을 내가 직접 클래스에 작성할 필요 없이 `authenticate()` 함수 하나로 그냥 끝나버리는 것... (약간 허무한거같기두 ㅎ)  

공식 문서에는 이렇게 나와있다.  


![image](https://user-images.githubusercontent.com/90256209/236618752-bd3c3149-b8b0-4272-a12a-02a942f8fe54.png)  


이번 기회로 로그인 및 사용자 인증에 대해 다시 자세히 복습해 볼 수 있어서 재밌었당!
