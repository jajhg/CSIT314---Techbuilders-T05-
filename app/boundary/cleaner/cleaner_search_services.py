from flask import Blueprint, render_template, request, session, redirect, url_for
from app.controller.cleaner.cleaner_search_services_controller import CleanerSearchController

search_bp = Blueprint('cleaner', __name__, url_prefix='/cleaner')

@search_bp.route('/search-services', methods=['GET', 'POST'])
def search_services():
    if 'user_id' not in session or session.get('user_type') != 'cleaner':
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        available_day = request.form.get('available_day')
        time_slot = request.form.get('time_slot')
        type_of_cleaning = request.form.get('type_of_cleaning')

        results = CleanerSearchController.search_services(
            cleaner_id=session['user_id'],
            available_day=available_day,
            time_slot=time_slot,
            type_of_cleaning=type_of_cleaning
        )
        return render_template('cleaner_search_results.html', services=results)

    options = CleanerSearchController.get_filter_options(session['user_id'])
    return render_template('cleaner_search_services.html', **options)