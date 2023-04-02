# CEOS 17기 백엔드 스터디  

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
