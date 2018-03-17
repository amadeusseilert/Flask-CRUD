from flask import Flask

from app.instance import db
from config import DevelopmentConfig


def create_app():
    app = Flask(__name__, template_folder='../app/templates')
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    from app.admin.views import admin as admin_bp
    app.register_blueprint(admin_bp)
    app.app_context().push()
    return app