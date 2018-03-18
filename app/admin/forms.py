from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange, InputRequired
from wtforms.widgets.html5 import NumberInput

from app.models import Vehicle


class AddVehicleForm(FlaskForm):
    v_type = SelectField('Type', choices=[(t, t) for t in Vehicle.VEHICLE_TYPES])
    manufacturer = StringField('Manufacturer', validators=[DataRequired(), Length(min=1, max=50)])
    model = StringField('Model', validators=[DataRequired(), Length(min=1, max=50)])
    color = StringField('Color', validators=[DataRequired(), Length(min=1, max=50)])
    engine = IntegerField('Engine (cc)', widget=NumberInput(), validators=[InputRequired(), NumberRange(min=1)])
    mileage = IntegerField('Mileage (km)', widget=NumberInput(), validators=[InputRequired(), NumberRange(min=0)])

    submit = SubmitField('Add')

    def __init__(self, *args, **kwargs):
        super(AddVehicleForm, self).__init__(*args, **kwargs)


class UpdateVehicleForm(FlaskForm):
    v_type = SelectField('Type', choices=[(t, t) for t in Vehicle.VEHICLE_TYPES])
    manufacturer = StringField('Manufacturer', validators=[DataRequired(), Length(min=1, max=50)])
    model = StringField('Model', validators=[DataRequired(), Length(min=1, max=50)])
    color = StringField('Color', validators=[DataRequired(), Length(min=1, max=50)])
    engine = IntegerField('Engine (cc)', widget=NumberInput(), validators=[InputRequired(), NumberRange(min=1)])
    mileage = IntegerField('Mileage (km)', widget=NumberInput(), validators=[InputRequired(), NumberRange(min=0)])

    submit = SubmitField('Update')

    def __init__(self, *args, **kwargs):
        super(UpdateVehicleForm, self).__init__(*args, **kwargs)

    def fill_form(self, vehicle):
        self.v_type.data = vehicle.v_type
        self.manufacturer.data = vehicle.manufacturer
        self.model.data = vehicle.model
        self.color.data = vehicle.color
        self.engine.data = vehicle.engine
        self.mileage.data = vehicle.mileage


def search_vehicles_form_builder(form):

    class SearchVehicleForm(FlaskForm):
        manufacturer = StringField('Manufacturer', validators=[Length(max=50)])
        model = StringField('Model', validators=[Length(max=50)])
        color = StringField('Color', validators=[Length(max=50)])
        min_engine = IntegerField('Min. Engine (cc)', widget=NumberInput(), default=50,
                                  validators=[InputRequired(), NumberRange(min=1)])
        max_engine = IntegerField('Max. Engine (cc)', widget=NumberInput(), default=2000,
                                  validators=[InputRequired(),  NumberRange(min=1)])
        min_mileage = IntegerField('Min. Mileage (km)', widget=NumberInput(), default=0,
                                   validators=[InputRequired(), NumberRange(min=0)])
        max_mileage = IntegerField('Max. Mileage (km)', widget=NumberInput(), default=200000,
                                   validators=[InputRequired(), NumberRange(min=0)])

        def validate(self):
            initial_validation = super(SearchVehicleForm, self).validate()
            if not initial_validation:
                return False

            if self.min_mileage.data > self.max_mileage.data:
                self.min_mileage.errors.append('Min. Mileage must be lower than Max. Mileage.')
                return False

            if self.max_mileage.data < self.min_mileage.data:
                self.min_mileage.errors.append('Max. Mileage must be higher than Min. Mileage.')
                return False

            if self.min_engine.data > self.max_engine.data:
                self.min_mileage.errors.append('Min. Engine must be lower than Max. Engine.')
                return False

            if self.max_engine.data < self.min_engine.data:
                self.min_mileage.errors.append('Max. Engine must be higher than Min. Engine.')
                return False

            return True

    for vt in Vehicle.VEHICLE_TYPES:
        setattr(SearchVehicleForm, vt, BooleanField(default=True, label=vt))

    setattr(SearchVehicleForm, 'submit', SubmitField('Go'))

    return SearchVehicleForm(form)
