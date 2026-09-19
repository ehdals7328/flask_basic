from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy #ORM 도구임

import config
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM Initialization
    db.init_app(app)
    migrate.init_app(app, db)

    # 해당 파일에 정의된 모든 모델 클래스를 애플리케이션에 등록
    from . import models

    # Blueprint
    from .views import main_views # 순환 참조를 막기 위한 Lazy Import
    app.register_blueprint(main_views.bp)

    from .views import sensor_views
    app.register_blueprint(sensor_views.bp)

    return app
