from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.utils import redirect

from app.admin.forms import AddVehicleForm, search_vehicles_form_builder, UpdateVehicleForm
from app.models import Vehicle
from app.instance import db


admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/', methods=['GET', 'POST'])
def index():
    form = search_vehicles_form_builder(request.form)
    type_fields = [getattr(form, vt) for vt in Vehicle.VEHICLE_TYPES]

    if form.validate_on_submit():
        types_search = [f.label.text for f in type_fields if f.data]
        manufacturer_search = form.manufacturer.data
        model_search = form.model.data
        color_search = form.color.data
        min_engine_search = form.min_engine.data
        max_engine_search = form.max_engine.data
        min_mileage_search = form.min_mileage.data
        max_mileage_search = form.max_mileage.data

        filtered_vehicles = Vehicle.perform_search(types_search, manufacturer_search, model_search, color_search,
                                                   min_engine_search, max_engine_search, min_mileage_search,
                                                   max_mileage_search)
        return render_template('index.html', form=form, vehicles=filtered_vehicles, types=type_fields)

    all_vehicles = Vehicle.query.all()
    return render_template('index.html', form=form, vehicles=all_vehicles, types=type_fields)


@admin.route('/add', methods=['GET', 'POST'])
def add():
    form = AddVehicleForm(request.form)
    if form.validate_on_submit():

        nv = Vehicle(
            form.v_type.data,
            form.manufacturer.data,
            form.model.data,
            form.color.data,
            form.engine.data,
            form.mileage.data
        )
        db.session.add(nv)
        db.session.commit()
        flash(nv.__repr__() + ' added.')
        return redirect(url_for('admin.add'))
    return render_template('vehicle.html', form=form)


@admin.route('/<int:vehicle_id>/delete', methods=['POST'])
def delete(vehicle_id):
    v = Vehicle.query.get_or_404(vehicle_id)  # type: Vehicle
    db.session.delete(v)
    db.session.commit()
    return redirect(url_for('admin.index'))


@admin.route('/<int:vehicle_id>/update', methods=['GET', 'POST'])
def update(vehicle_id):
    v = Vehicle.query.get_or_404(vehicle_id)  # type: Vehicle
    form = UpdateVehicleForm(request.form)
    if request.method == 'GET':
        form.fill_form(v)
        return render_template('vehicle.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            v.v_type = form.v_type.data
            v.manufacturer = form.manufacturer.data
            v.model = form.model.data
            v.color = form.color.data
            v.engine = form.engine.data
            v.mileage = form.mileage.data

            db.session.commit()
            return redirect(url_for('admin.index'))

    return redirect(url_for('admin.update', vehicle_id=v.id))
