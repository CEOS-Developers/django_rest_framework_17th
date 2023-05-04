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
