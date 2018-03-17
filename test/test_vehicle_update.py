from unittest import TestCase

from app.admin.forms import AddVehicleForm
from app.models import Vehicle, VehicleTypes
from test_util import create_app

from app.instance import db


class TestVehicleAdd(TestCase):

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

    def test_add_vehicle_get(self):
        response = self.test_client.get('/add')
        self.assertEqual(response._status_code, 200)

    def test_add_vehicle_post(self):

        form = AddVehicleForm(formdata=None)
        form.v_type.data = VehicleTypes('Car').name
        form.manufacturer.data = 'Honda'
        form.model.data = 'Civic'
        form.color.data = 'White'
        form.engine.data = 1800
        form.mileage.data = 4000

        self.assertEqual(len(Vehicle.query.all()), 0)

        with self.test_client.session_transaction():
            response = self.test_client.post('/add', data=form.data, follow_redirects=True)

        v = Vehicle.query.filter(Vehicle.model == 'Civic').one_or_none()
        self.assertEqual(response._status_code, 200)
        self.assertEqual(len(Vehicle.query.all()), 1)
        self.assertIsNotNone(v)
