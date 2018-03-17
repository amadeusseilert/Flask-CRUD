from unittest import TestCase

from app.admin.forms import UpdateVehicleForm
from app.models import Vehicle
from test_util import create_app

from app.instance import db


class TestVehicleUpdate(TestCase):

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

    def test_update_vehicle_post(self):

        v1 = Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)

        self.db.session.add(v1)
        self.db.session.commit()

        form = UpdateVehicleForm(formdata=None, obj=v1)
        form.v_type.data = 'Motorcycle'
        form.manufacturer.data = 'Yamaha'
        form.model.data = 'Tenere'
        form.engine.data = 250

        with self.test_client.session_transaction():
            response = self.test_client.post('/' + str(v1.id) + '/update', data=form.data, follow_redirects=True)

        self.assertEqual(response._status_code, 200)
        self.assertEqual(v1.v_type, 'Motorcycle')
        self.assertEqual(v1.manufacturer, 'Yamaha')
        self.assertEqual(v1.model, 'Tenere')
        self.assertEqual(v1.engine, 250)
