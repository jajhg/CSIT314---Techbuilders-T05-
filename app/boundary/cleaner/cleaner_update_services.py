from flask import Blueprint, abort, render_template, request, session, flash, redirect, url_for
from app.controller.cleaner.cleaner_update_services_controller import ServiceUpdateController

update_bp = Blueprint('update', __name__, url_prefix='/services')

@update_bp.route('/<int:service_id>/update', methods=['GET', 'POST'])
def update_service(service_id):
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
            'type_of_cleaning': request.form.get('type_of_cleaning'),
            'supplies': request.form.get('supplies'),
            'languages': request.form.get('languages')
        }

        success, message = ServiceUpdateController.update_service(service_id, session['user_id'], service_data)
        if success:
            flash(message, "success")
            return redirect(url_for('cleaner.dashboard'))
        else:
            flash(message, "error")
    
    service = ServiceUpdateController.get_service_for_update(service_id, session['user_id'])
    if not service:
        abort(404)
        
    context = ServiceUpdateController.get_update_form_options()
    return render_template("cleaner_update_service.html", service=service, **context)