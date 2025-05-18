from flask import Blueprint, request, session, flash, redirect, url_for
from app.controller.cleaner.cleaner_delete_services_controller import ServiceDeleteController

delete_service_bp = Blueprint('delete_service', __name__, url_prefix='/services')

@delete_service_bp.route('/<int:service_id>/delete', methods=['POST'])
def delete_service(service_id):
    if 'user_id' not in session or session.get('user_type') != 'Cleaner': 
        flash('Please log in as a cleaner.', 'warning')
        return redirect(url_for('login'))

    success, message = ServiceDeleteController.delete_service(service_id, session['user_id'])
    if success:
        flash(message, "success")
    else:
        flash(message, "error")
    
    return redirect(url_for('cleaner_dashboard'))