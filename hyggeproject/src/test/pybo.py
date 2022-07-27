from flask import Flask

app = Flask(__name__)
# FLASK 어플리케이션 생성 코드
# __name__ : 모듈명 저장
# 즉 이 파일이 실행되면 pybo.py 라는 모듈이 실행되는 것이므로 모듈명 'pybo' 저장됨

@app.route('/')   
# URL과 플라스크 코드를 매핑하는 플라스크 데코레이터
# 즉 api를 생성시킴
def hello_pybo():
    return 'Hello, pybo'