
## 플라스크 프로젝트 사용방법

- 터미널 아나콘다 설치 후 진행
- 가상환경 생성 및 실행

```
cd C:\Users\20200\Desktop\hygge
mkdir services
cd services
mkdir web
cd web
python -m venv hyggevenv   //가상환경 생성
cd hyggevenv/Scripts
activate   //가상환경 실행
(hyggevenv) (base) C:\Users\20200\Desktop\hygge\services\web\hyggevenv\Scripts>
```

- 가상환경 내에서 flask 실행하기

```
(python -m) pip install --upgrade pip
pip install flask
export FLASK_APP=project/__init__.py
** windows의 경우 export가 아니라 set 사용
flask run

-> gunicorn 사용의 경우 gunicorn --bind 0.0.0.0:5000 파일명:app
```

- docker-compose로 flask 실행하기

```
cd (docker-compose 파일 위치)
docker-compose build (이미지 빌드)
docker-compose up -d (이미지 기반 컨테이너 실행)
-> docker-compose up -d --build

-> 이미 컨테이너가 생성됐으면 docker-compose up 하면 사용가능

1. 플라스크 접속
웹사이트 localhost:5000
2. DB 접속
docker-compose exec db psql --username=postgres --dbname=hygge_db
** 오류가 발생하는 경우 로그 확인
docker-compose logs -f
```
