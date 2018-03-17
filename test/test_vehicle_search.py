from unittest import TestCase

from flask import Flask

from app.instance import db
from app.models import Vehicle, VehicleTypes
from config import DevelopmentConfig


class TestAdminListAll(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @staticmethod
    def create_app():
        app = Flask(__name__, template_folder='../app/templates')
        app.config.from_object(DevelopmentConfig)
        db.init_app(app)

        from app.admin.views import admin as admin_bp
        app.register_blueprint(admin_bp)
        app.app_context().push()
        return app

    def setUp(self):
        self.app = self.create_app()
        self.test_client = self.app.test_client()
        self.db = db
        self.db.create_all()
        self.db.session.commit()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_search(self):
        v1 = Vehicle(VehicleTypes.CAR, u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = Vehicle(VehicleTypes.CAR, u'Volkswagen', u'Fox', u'Silver', 1600, 10000)

        self.db.session.add(v1)
        self.db.session.add(v2)
        self.db.session.commit()

        Vehicle.perform_search(['Car'], 'Car', '')