from unittest import TestCase
from app.instance import db
from app.models import Vehicle
from test_util import create_app


class TestVehicleSearch(TestCase):

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

    def test_search_type_1(self):
        v1 = Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = Vehicle(u'Car', u'Volkswagen', u'Fox', u'Silver', 1600, 10000)

        self.db.session.add(v1)
        self.db.session.add(v2)
        self.db.session.commit()

        vv = Vehicle.perform_search(['Motorcycle'], '', '', '', 1, 10000, 0, 200000)
        self.assertEqual(len(vv), 0)

    def test_search_type_2(self):
        v1 = Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = Vehicle(u'Motorcycle', u'Honda', u'CG 125', u'Silver', 125, 10000)

        self.db.session.add(v1)
        self.db.session.add(v2)
        self.db.session.commit()

        vv = Vehicle.perform_search(['Motorcycle'], '', '', '', 1, 10000, 0, 200000)
        self.assertEqual(len(vv), 1)
        self.assertEqual(vv[0].id, v2.id)

    def test_search_manufacturer(self):
        v1 = Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = Vehicle(u'Motorcycle', u'Honda', u'CG 125', u'Silver', 125, 10000)
        v3 = Vehicle(u'Car', u'Honda', u'Civic', u'Silver', 1600, 10000)

        self.db.session.add(v1)
        self.db.session.add(v2)
        self.db.session.add(v3)

        self.db.session.commit()

        vv = Vehicle.perform_search(['Motorcycle', 'Car'], 'Honda', '', '', 1, 10000, 0, 200000)
        self.assertEqual(set(vv), {v2, v3})

    def test_search_model(self):
        v1 = Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = Vehicle(u'Motorcycle', u'Honda', u'CG 125', u'Silver', 125, 10000)

        self.db.session.add(v1)
        self.db.session.add(v2)

        self.db.session.commit()

        vv = Vehicle.perform_search(['Motorcycle', 'Car'], '', 'Uno', '', 1, 10000, 0, 200000)
        self.assertEqual(len(vv), 1)
        self.assertEqual(vv[0].id, v1.id)

    def test_search_engine_range_1(self):
        v1 = Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = Vehicle(u'Motorcycle', u'Honda', u'CG 125', u'Silver', 125, 10000)

        self.db.session.add(v1)
        self.db.session.add(v2)

        self.db.session.commit()

        vv = Vehicle.perform_search(['Motorcycle', 'Car'], '', '', '', 126, 10000, 0, 200000)
        self.assertEqual(len(vv), 1)
        self.assertEqual(vv[0].id, v1.id)

    def test_search_engine_range_2(self):
        v1 = Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = Vehicle(u'Motorcycle', u'Honda', u'CG 125', u'Silver', 125, 10000)

        self.db.session.add(v1)
        self.db.session.add(v2)

        self.db.session.commit()

        vv = Vehicle.perform_search(['Motorcycle', 'Car'], '', '', '', 1, 125, 0, 200000)
        self.assertEqual(len(vv), 1)
        self.assertEqual(vv[0].id, v2.id)

    def test_search_mileage_range_1(self):
        v1 = Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = Vehicle(u'Motorcycle', u'Honda', u'CG 125', u'Silver', 125, 10000)

        self.db.session.add(v1)
        self.db.session.add(v2)

        self.db.session.commit()

        vv = Vehicle.perform_search(['Motorcycle', 'Car'], '', '', '', 1, 10000, 0, 0)
        self.assertEqual(len(vv), 1)
        self.assertEqual(vv[0].id, v1.id)

    def test_search_mileage_range_2(self):
        v1 = Vehicle(u'Car', u'Fiat', u'Uno', u'Red', 1000, 0)
        v2 = Vehicle(u'Motorcycle', u'Honda', u'CG 125', u'Silver', 125, 10000)

        self.db.session.add(v1)
        self.db.session.add(v2)

        self.db.session.commit()

        vv = Vehicle.perform_search(['Motorcycle', 'Car'], '', '', '', 1, 10000, 10000, 200000)
        self.assertEqual(len(vv), 1)
        self.assertEqual(vv[0].id, v2.id)
