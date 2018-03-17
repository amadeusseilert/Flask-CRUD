from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.utils import redirect

from app.admin.forms import NewVehicleForm, search_vehicles_form_builder
from app.models import Vehicle, VehicleTypes
from app.instance import db


admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/', methods=['GET', 'POST'])
def list_all():
    form = search_vehicles_form_builder(request.form)
    type_fields = [getattr(form, vt.name) for vt in VehicleTypes]

    if form.validate_on_submit():
        types_search = {f.label.text: f.data for f in type_fields}
        manufacturer_search = form.manufacturer.data
        model_search = form.model.data
        min_engine_search = form.min_engine.data
        max_engine_search = form.max_engine.data
        min_mileage_search = form.min_mileage.data
        max_mileage_search = form.max_mileage.data
        return redirect(url_for('admin.list_all'))

    all_vehicles = Vehicle.query.all()
    return render_template('admin/list.html', form=form, vehicles=all_vehicles, types=type_fields)


@admin.route('/add', methods=['GET', 'POST'])
def add_vehicle():
    form = NewVehicleForm(request.form)
    if form.validate_on_submit():

        nv = Vehicle(
            VehicleTypes[form.type.data],
            form.manufacturer.data,
            form.model.data,
            form.engine.data,
            form.mileage.data
        )
        db.session.add(nv)
        db.session.commit()
        flash(nv.__repr__() + ' added.')
        return redirect(url_for('admin.add_vehicle'))
    return render_template('admin/add.html', form=form)
