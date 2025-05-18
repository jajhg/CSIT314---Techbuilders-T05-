from flask import Blueprint, render_template, request, session, url_for, redirect, abort
from ...controller.cleaner.cleaner_view_services_controller import CleanerServiceController

cleaner_bp = Blueprint('cleaner', __name__, url_prefix='/cleaner')

@cleaner_bp.route('/dashboard')
def cleaner_dashboard():
    if 'user_id' not in session or session.get('user_type') != 'cleaner':
        return redirect(url_for('auth.login'))
    
    services = CleanerServiceController.get_services(session['user_id'])
    return render_template('cleaner_dashboard.html', services=services)

@cleaner_bp.route('/service/<int:service_id>')
def view_service(service_id):
    if 'user_id' not in session or session.get('user_type') != 'cleaner':
        return redirect(url_for('auth.login'))
    
    service = CleanerServiceController.get_service(service_id, session['user_id'])
    if not service:
        abort(404)
    
    return render_template('cleaner_view_service.html', service=service)