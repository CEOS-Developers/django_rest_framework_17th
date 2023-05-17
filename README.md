# 6주차 : AWS : https 인증

- 지난 과제 하고 느낀건데 에러나는거 다 적고 하다보면 정리가 아니라 일기가 되어버린다..
- 그리고 발표 길면 재미없으니까 양보단 질로 승부하겠다.

- 프로젝트 배포했는데 http인거 보면 좀 불편하긴 했다

# HTTPS

> HTTPS := HTTP + (Secure Socket Layer(SSL) | Transport Layer Security(TLS))

## SSL

- 메세지 인증으로 MAC 사용
- 더이상 쓰지 않음 (보안의 취약점, 느린 속도)
  - TLS를 SSL로 부르기도 한다고 합니다



## TLS

- SSL보다 적은 단계로 프로세스 속도가 비교적 빠름
- 암호화 알고리즘을 SSL에서 발전시켜 보안성 강화
- 메세지 인증으로 HMAC 사용
- 업계 표준

### TLS Handshake

<img width="362" alt="image" src="https://github.com/CEOS-Developers/django_rest_framework_17th/assets/76674422/bf6a2a77-af58-48d0-afb5-d86d00a7e2bb">

[출처 IBM Docs](https://www.ibm.com/docs/en/ibm-mq/9.1?topic=tls-overview-ssltls-handshake)

- 클라이언트가 _Client Hello_ 송신
  - 사용할 TLS 버전, 클라이언트가 지원하는 CipherSuite, 무작위 바이트 문자열을 포함
- 서버가 _Server Hello_ 송신
  - 클라이언트가 지원하는 CipherSuite중 하나, 세션ID, 무작위 바이트 문자열을 포함 
- 서버가 Server Certificate도 송신함 ( 디지털 서명 )
- 클라이언트가 서버의 'Client Certificate 요청'에 따라 Client Certificate 송신
- 클라이언트가 연결에 쓰일 비밀 키 송신함 (무작위 바이트 문자열으로 만듦)
- 서버가 Client Certificate를 검증하고 비밀 키로 암호화된 _Finished_ 송신
- 클라이언트가 비밀 키로 암호화된 _Finished_ 송신

# HTTPS 설정

## ALB(ELB) : Load Balancer

- 웹 서비스에 걸리는 부하를 분산해준다

### ELB : Elasitc Load Balancer

- 4계층(Transport Layer)과 7계층(Application Layer)에서 동작한다
- 이제 Classic Load Balancer(CLB)라고도 부른다
- 포괄적으로 ALB도 ELB라고 부른다

### ALB : Application Load Balancer

- 7계층에서만 동작
- WebSocket 및 HTTP/2 지원
- 직접 인스턴스화 되는 ELB와 달리 서비스를 독립적으로 실행 가능
- 여러 라우팅 규칙 정의 가능

#### ELB --> ALB 변경시 이점

- 여러개의 로드밸런서를 통합하여 비용 절감
- WebSocket, HTTP/2 등으로 성능 향상
- AWS WAF(Web Application Firewall)를 통한 보안 강화

##### 추가) NLB : Network Load Balancer

- 4계층에서만 동작
  - 네트워크 패의 검사 없이 부하를 분산
- 고성능을 요구하는 환경에서 적합

## 구현
<img width="883" alt="image" src="https://github.com/CEOS-Developers/django_rest_framework_17th/assets/76674422/e46dcb00-e23d-495b-b0a9-39c1b444635f">

[출처 tistory](https://moondol-ai.tistory.com/467)

- `Web Server(nginx)`와 `Clients` 사이에 `ALB(ELB)`를 끼워넣는다
- 443 포트로 들어오는 HTTPS 요청을 처리한다
- 80 포트로 들어오는 HTTP 요청을 443 포트로 리다이렉트 시킨다

### 1️⃣ AWS의 Route 53에서 원하는 도메인을 구입한다.

- 가비아로 `ceos-popcoder.store`/1년 구입 (500원 이라서 `.store`로 했다..)

### 2️⃣ AWS의 Certificate Manager에서 원하는 도메인에 대한 SSL 인증서를 받는다.

<img width="826" alt="image" src="https://github.com/CEOS-Developers/django_rest_framework_17th/assets/76674422/4129b879-d905-4bab-9e22-35634b9ecc21">

#### FQDN
<img width="991" alt="image" src="https://github.com/CEOS-Developers/django_rest_framework_17th/assets/76674422/46b8f7ed-8329-483d-9caa-158748f8458a">

[출처 AWS Docs](https://docs.aws.amazon.com/ko_kr/acm/latest/userguide/acm-certificate.html)

- **TL;DR**: 와일드카드는 하나의 하위 도메인 수준만 보호할 수 있다. (`*.ceos-popcoder.store`는 `ceos-popcoder.store`를 보호할 수 없다.)
- 위와 같은 이유로 `ceos-popcoder.store`, `*.ceos-popcoder.store`를 입력한다.

#### RSA
<img width="529" alt="image" src="https://github.com/CEOS-Developers/django_rest_framework_17th/assets/76674422/5666aadd-7dcf-49f1-a1e5-621ed33ad9eb">

- 공개키 암호 알고리 중의 하나로, TLS 연결 간 암호화 방식을 선택할 수 있다

#### Route 53에 레코드 생성

- AWS Certificate Manager에서 요청한 인증서 클릭 -> 하단 도메인 탭에서 CNAME 확인
- Route 53에서 레코드 생성

<img width="1069" alt="image" src="https://github.com/CEOS-Developers/django_rest_framework_17th/assets/76674422/3e796d0e-a53a-471f-b666-5e0289229104">

- 발급됨 확인

### 3️⃣ 서버로 사용할 Ec2 인스턴스에 대해서 Elastic Load Balancer(로드밸런서)를 등록한다.

<img width="1158" alt="image" src="https://github.com/CEOS-Developers/django_rest_framework_17th/assets/76674422/c1715d70-951a-4697-bb66-9763773f79c8">

- 로드밸런서 등록 완료 (스터디 자료 참고)

### 4️⃣ 80번 포트로 들어오는 요청은 Redirect, 443번 포트로 들어오는 요청을 인스턴스로 연결해준다.

<img width="1243" alt="image" src="https://github.com/CEOS-Developers/django_rest_framework_17th/assets/76674422/e46e8ce7-ca2d-4c86-b2c7-fea4a761a169">

```shell
# nginx.conf
if ($http_x_forwarded_proto != 'https') {
	return 301 https://$host$request_uri;
}
```

- 리디렉션 로직을 ALB와 nginx에서 구현

### 5️⃣ 등록한 로드밸런서를 AWS Route 53의 도메인의 레코드에 등록한다.

<img width="1013" alt="image" src="https://github.com/CEOS-Developers/django_rest_framework_17th/assets/76674422/448a46a8-e4e6-4329-af00-a4e5f58d6e71">

- A 레코드 등록 완료

### 6️⃣ ec2 인바운드 규칙 443 추가

<img width="1142" alt="image" src="https://github.com/CEOS-Developers/django_rest_framework_17th/assets/76674422/8f9799fd-3361-4e5d-85a1-a1a63657347d">

- HTTPS 인바운드 규칙 추가 완료

