from app.instance import db
from enum import Enum


class VehicleTypes(Enum):
    CAR = 'Car'
    MOTORCYCLE = 'Motorcycle'


class Vehicle(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    manufacturer = db.Column(db.String(50))
    model = db.Column(db.String(50))
    engine = db.Column(db.Integer)
    mileage = db.Column(db.Integer)

    def __init__(self, v_type=VehicleTypes.CAR, manufacturer='', model='', engine=1, mileage=0):
        # SQLite does not support Enum
        self.type = v_type.value
        self.manufacturer = manufacturer
        self.model = model
        self.engine = engine
        self.mileage = mileage

    def __repr__(self):
        return 'Vehicle - {} {} {}'.format(self.manufacturer, self.model, self.engine)

    @property
    def engine_label(self):
        if self.type == 'Car':
            return '{:.1f}'.format(self.engine / 1000.0)
        else:
            return '{} cc'.format(self.engine)

    @property
    def mileage_label(self):
        if self.mileage == 0:
            return 'NEW'
        else:
            return str(self.mileage)
