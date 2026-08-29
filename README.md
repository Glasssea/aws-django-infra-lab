## 프로젝트를 다시 배포한 이유

과거 웹 개발 과정에서 Django 프로젝트를 직접 제작하고 배포하면서
서버, 데이터베이스, 도메인, 웹 서버 설정 등을 함께 경험했습니다.

당시에는 웹서비스를 동작시키기 위해 필요한 기술을 하나씩 익혔을 뿐,
이 경험들이 서버와 네트워크 인프라 역량과 연결된다는 점은 크게 생각하지 못했습니다.

이후 네트워크와 서버 인프라를 공부하면서,
과거에 직접 구성했던 환경을 다시 이해하고 정리해보고자
기존 Django 프로젝트를 AWS EC2 Ubuntu 환경에 재배포했습니다.

## Infrastructure Architecture

```text
Client
  ↓ HTTP / 80
AWS EC2 (Ubuntu)
  ↓
Nginx
  ↓ Unix Socket
Gunicorn
  ↓
Django
  ↓
MySQL


## Tech Stack

- AWS EC2
- Ubuntu Linux
- Nginx
- Gunicorn
- Django
- MySQL
- Git / GitHub



## Deployment Details

- AWS EC2 Ubuntu 인스턴스 구성
- Security Group을 통한 SSH(22), HTTP(80) 접근 제어
- Nginx를 Reverse Proxy로 구성
- Gunicorn을 systemd 서비스로 등록하여 Django 애플리케이션 실행
- Unix Socket을 통해 Nginx와 Gunicorn 연동
- MySQL 데이터베이스 구성 및 Django 연결
- Elastic IP를 사용하여 고정 Public IP 구성
- Django static 파일을 collectstatic 후 Nginx에서 직접 제공


## Troubleshooting

### Static 파일 403 오류
Nginx에서 static 파일을 제공하도록 설정한 뒤 403 Forbidden 오류가 발생했습니다.

원인을 확인한 결과 Nginx 실행 사용자(`www-data`)가
`/home/ubuntu` 디렉토리를 통과할 권한이 없어 static 파일에 접근하지 못하고 있었습니다.

디렉토리 권한을 조정하여 Nginx가 필요한 경로에 접근할 수 있도록 수정했고,
이후 static 파일이 정상적으로 제공되는 것을 확인했습니다.


## Service

AWS EC2 환경에서 현재 서비스가 실행되고 있습니다.
