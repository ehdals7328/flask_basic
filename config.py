import os

BASE_DIR = os.path.dirname(__file__) # 현재 config.py 파일의 경로를 저장함.
print("BASE_DIR:", BASE_DIR) # 확인용
# sqlite는 파일기반 DB (스키마, 데이터)이므로 하나의 파일(pybo.db)이 필요함
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, "pybo.db"))
# sqlite:///는 sqlite://에 절대 경로인 / 을 설정함 (SQLite 접속 주소)
print("SQLALCHEMY_DATABASE_URI:", SQLALCHEMY_DATABASE_URI) # 확인용
SQLALCHEMY_TRACK_MODIFICATIONS = False # (SQLAlchemy의 객체 변경 사항을 추적하여 신호를 발생시키는 기능)
# 이벤트 처리 옵션으로 필요하지 않아 False 로 셋팅함.