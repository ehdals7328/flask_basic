import os
import oracledb

from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.dirname(__file__) # 현재 파일의 경로를 저장함
print("BASE_DIR", BASE_DIR)

SQLALCHEMY_DATABASE_URI = "oracle+oracledb://scott:tiger@localhost:1521/xe"
#[DB종류]+[파이썬드라이버]://[아이디]:[비밀번호]@[서버주소]:[포트번호]/[DB이름]

print("SQLALCHEMY_DATABASE_URI", SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLAlchemy의 객체 변경 사항을 추적하여 신호를 발생시키는 기능임
# 이벤트 처리 옵션으로 필요하지 않아 False로 셋팅함.
SECRET_KEY = 'dev'
# xe 에러시 xepdb1
