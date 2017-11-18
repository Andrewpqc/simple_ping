from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config

db=SQLAlchemy()

#工厂函数
def create_app(config_key):
    app=Flask(__name__)
    app.config.from_object(config[config_key])

    config[config_key].init_app(app)
    db.init_app(app)

    #注册蓝图
    from .service import service as service_blueprint
    app.register_blueprint(service_blueprint, url_prefix="/service")

    return app




