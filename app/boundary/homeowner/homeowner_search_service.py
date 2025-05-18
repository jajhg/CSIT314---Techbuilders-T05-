from flask import Blueprint, render_template, request, session, redirect, url_for
from app.controller.homeowner.homeowner_search_service_controller import HomeownerSearchController

homeowner_bp = Blueprint('homeowner', __name__, url_prefix='/homeowner')

@homeowner_bp.route('/search-services', methods=['GET', 'POST'])
def search_services():
    if 'user_id' not in session or session.get('user_type') != 'HomeOwner':
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        filters = {
            'available_day': request.form.get('available_day'),
            'time_slot': request.form.get('time_slot'),
            'type_of_cleaning': request.form.get('type_of_cleaning')
        }
        results = HomeownerSearchController.search_services(filters)
        return render_template('homeowner_search_results.html', services=results)

    options = HomeownerSearchController.get_filter_options()
    return render_template('homeowner_search_services.html', **options)