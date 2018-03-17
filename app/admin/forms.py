from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, BooleanField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired, Length, NumberRange, InputRequired


from app.models import VehicleTypes


class NewVehicleForm(FlaskForm):
    type = SelectField('Type', choices=[(t.name, t.value) for t in VehicleTypes])
    manufacturer = StringField('Manufacturer', validators=[DataRequired(), Length(min=1, max=50)])
    model = StringField('Model', validators=[DataRequired(), Length(min=1, max=50)])
    engine = IntegerField('Engine (cc)', validators=[InputRequired(), NumberRange(min=1)])
    mileage = IntegerField('Mileage (km)', validators=[InputRequired(), NumberRange(min=0)])

    submit = SubmitField('Add')

    def __init__(self, *args, **kwargs):
        super(NewVehicleForm, self).__init__(*args, **kwargs)


def search_vehicles_form_builder(form):

    class SearchVehicleForm(FlaskForm):
        manufacturer = StringField('Manufacturer', validators=[Length(max=50)])
        model = StringField('Model', validators=[Length(max=50)])
        min_engine = IntegerField('Min. Engine (cc)', default=1000, validators=[NumberRange(min=1)])
        max_engine = IntegerField('Max. Engine (cc)', default=2000, validators=[NumberRange(min=1)])
        min_mileage = IntegerField('Min. Mileage (km)', default=0, validators=[NumberRange(min=0)])
        max_mileage = IntegerField('Max. Mileage (km)', default=200000, validators=[NumberRange(min=0)])

    for vt in VehicleTypes:
        setattr(SearchVehicleForm, vt.name, BooleanField(default=True, label=vt.value))

    setattr(SearchVehicleForm, 'submit', SubmitField('Go'))

    return SearchVehicleForm(form)
