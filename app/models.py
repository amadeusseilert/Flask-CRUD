from app.instance import db


class Vehicle(db.Model):

    VEHICLE_TYPES = ['Car', 'Motorcycle']

    id = db.Column(db.Integer, primary_key=True)
    v_type = db.Column(db.String(50))
    manufacturer = db.Column(db.String(50))
    model = db.Column(db.String(50))
    color = db.Column(db.String(50))
    engine = db.Column(db.Integer)
    mileage = db.Column(db.Integer)

    def __init__(self, v_type, manufacturer, model, color, engine, mileage):
        # SQLite does not support Enum
        self.v_type = v_type
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.engine = engine
        self.mileage = mileage

    def __repr__(self):
        return 'Vehicle - {} {} {}'.format(self.manufacturer, self.model, self.engine)

    @classmethod
    def perform_search(cls, types, manufacturer, model, color, min_engine, max_engine, min_mileage, max_mileage):

        q = cls.query.filter(
            cls.v_type.in_(types)
        ).filter(
            cls.engine >= min_engine,
            cls.engine <= max_engine
        ).filter(
            cls.mileage >= min_mileage,
            cls.mileage <= max_mileage)

        if color:
            q = q.filter(cls.color.ilike('%' + color + '%'))

        if manufacturer:
            q = q.filter(cls.manufacturer.ilike('%' + manufacturer + '%'))

        if model:
            q = q.filter(cls.model.ilike('%' + model + '%'))

        return q.all()

    @property
    def engine_label(self):
        if self.v_type == 'Car':
            return '{:.1f}'.format(self.engine / 1000.0)
        else:
            return '{} cc'.format(self.engine)

    @property
    def mileage_label(self):
        if self.mileage == 0:
            return 'NEW'
        else:
            return str(self.mileage)
