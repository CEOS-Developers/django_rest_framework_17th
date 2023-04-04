# CEOS 17기 백엔드 스터디

## 구현 기능
   : 1) boards : 글쓰기, 클릭한 게시물 보기, 모든 게시물 보기
     2) accounts : 로그인, 로그아웃, 회원가입
     3) comments : 게시글에 댓글 달기
     4) tags : 태그 기능은 게시글을 작성할때 그글이 포함되어 있는 내용을 단어로 요약한것입니다. 게시글을 작성할때마다 개수의 제한 없이 태그를 입력받을수 있고 입력받은 값을 저장하되 기존에 겹치는 태그는 늘리지 저장이아닌 불러오는 형식으로 구현했습니다.
     5) timetables :시간표 만들기(강의 등록 등), 친구맺기, 과목 등록하기
   
## 겪은 오류와 해결 과정
  1) error code 1046 : No database selected : **use [schema 이름];** 을 빼먹었다 ;; 즉 어떤 스키마에 데이터베이스를 설치할 지 정해주며 테이블 생성을 시작해야한다.
  2) error code 1824 : Failed to open the referenced table ‘board’ : article table을 만들려다가 오류가 났다. 이유는 데이터베이스들은 ‘관계형’이다. 따라서 생성되는 순서가 중요하다. board가 있어야 article이 존재할 수 있다. 생성 순서 중요 
  3) error code 1072 : column을 먼저 추가한 후 key 값으로 설정할 수 있음. 이거 안해서 계속 에러 뜸..  
  4) error code 1681 : mysql이 더 이상 int에 length를 정하는 것을 지원하지 않는다. 따라서 int 옆에 적어준 길이를 지정하지 않았더니 해결됐다.
  5) RuntimeError : Model class boards.models.Board doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS 
    이런 류의 에러가 자꾸만 떠서 고생을 많이 했다… ㅠ 이때는 [settings.py](http://settings.py) 나 이번 과제의 경우 [base.py](http://base.py) 에 들어가면서 INSTALLED_APPS 에 내가 빠뜨린 앱이 없는지 살펴보면 된다.
  6) page not found 오류 : runserver를 했지만 페이지가 안떴다. 이 때 path('',home)을 해주니 로그인 해주세요! 라는 문구가 뜨면서 해결이 됐다.

## 새롭게 배운 점
  1) .env 파일은 보안을 유지하기 위해 설정하는 파일로 dev.py를 바꾸면 안된다고 한다…
  2) 자동증가 : 스키마를 작성하다보면 데이터의 수를 p.k로 설정해야 할때가 있다. 이럴경우 새로 데이터를 insert할때마다 max(num)으로 기존에 추가되어있는 num의 최대값을 알아야 p.k값이 겹치지 않게 추가를 할 수있다. 하지만 *insert마다 이렇게 num의 최대값을 받아오는 sql문을 작성하는것은 비효율적*이므로 num에 Auto_Increment 속성으로 insert문을 보낼때 마다 자동으로 num값이 증가되게 저장할 수 있다.
  3) ERD 추출하기 : MySQL 이 알아서 추출해준다 !_! 완전 신기하다 (feat. 재령)
  4)
   python [manage.py](http://manage.py/) makemigrations accounts
   python [manage.py](http://manage.py/) migrate accounts
   python [manage.py](http://manage.py/) migrate

  1번의 경우, accounts/models.py에 저장한 모델을 등록전 테이블 양식을 생성해주는것이다.
  2번의 경우, 생성해준 테이블양식을 적용하는 절차이다.
  3번의 경우, 앱의 모델이 아닌 전에 설정한 settings.py와 그 외의 데이터베이스에 들어갈 
   변경사항을 적용시키는 절차이다.

## 궁금한 점

## 느낀 점
  : 다른 일정과 몸살이 겹쳐서 과제를 시간 안에 완벽하게 완수하지 못한 게 아쉽지만 그래도 끝까지 포기 안하고 대부분의 모델링은 구현해서
    다행이라고 생각했습니다.

## 회고
 좀 더 자세한 과정 및 회고는 노션 링크로 달아두었습니다.
 https://thin-pangolin-e02.notion.site/Django-2-0412d38d89ca40e6ace5c91621d5c819
