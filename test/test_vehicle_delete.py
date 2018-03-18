from unittest import TestCase

from app.models import Vehicle
from test_util import create_app

from app.instance import db


class TestVehicleDelete(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = create_app()
        self.test_client = self.app.test_client()
        self.db = db
        self.db.create_all()
        self.db.session.commit()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_delete_vehicle_post(self):
        v1 = Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = Vehicle(u'Car', u'Volkswagen', u'Fox', u'Silver', 1600, 10000)

        self.db.session.add(v1)
        self.db.session.add(v2)
        self.db.session.commit()

        with self.test_client.session_transaction():
            response = self.test_client.post('/' + str(v2.id) + '/delete', follow_redirects=True)

        v = Vehicle.query.filter(Vehicle.model == u'Fox').one_or_none()
        self.assertEqual(response._status_code, 200)
        self.assertEqual(len(Vehicle.query.all()), 1)
        self.assertIsNone(v)
