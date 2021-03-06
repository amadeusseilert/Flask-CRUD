from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config):
    new_app = Flask(__name__)
    new_app.config.from_object(config)

    db.init_app(new_app)

    from admin.views import admin as admin_bp
    new_app.register_blueprint(admin_bp, url_prefix='/admin')

    from main.views import main as main_bp
    new_app.register_blueprint(main_bp)

    return new_app


def init_db(config):
    app = create_app(config)
    with app.app_context():

        import models

        db.drop_all()
        db.create_all()
        db.session.commit()

        v1 = models.Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = models.Vehicle(u'Car', u'Volkswagen', u'Fox', u'Silver', 1600, 10000)
        v3 = models.Vehicle(u'Motorcycle', u'BMW', u'G 310 R', u'White', 313, 5000)

        db.session.add(v1)
        db.session.add(v2)
        db.session.add(v3)

        db.session.commit()
