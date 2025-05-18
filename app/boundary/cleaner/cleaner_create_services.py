from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from app.controller.cleaner.cleaner_create_services_controller import ServiceController

service_bp = Blueprint('service', __name__, url_prefix='/services')

@service_bp.route('/create', methods=['GET', 'POST'])
def create_service():
    if 'user_id' not in session or session.get('user_type') != 'cleaner':
        flash('Please log in as a cleaner.', 'warning')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        service_data = {
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'location': request.form.get('location'),
            'postal_code': request.form.get('postal_code'),
            'rate': request.form.get('rate'),
            'rate_type': request.form.get('rate_type'),
            'min_hours': request.form.get('min_hours'),
            'days_available': request.form.getlist('days_available'),
            'time_slots': request.form.getlist('time_slots'),
            'cleaning_types': request.form.getlist('cleaning_types'),
            'supplies': request.form.get('supplies'),
            'languages': request.form.get('languages')
        }

        success, message = ServiceController.create_service(session['user_id'], service_data)
        if success:
            flash(message, "success")
            return redirect(url_for('cleaner.dashboard'))
        else:
            flash(message, "error")

    context = ServiceController.get_service_form_options()
    return render_template("cleaner_create_service.html", **context)