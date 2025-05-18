from flask import Blueprint, render_template, request, session
from app.controller.homeowner.homeowner_shortlist_controller import HomeownerShortlistController

homeowner_shortlist_bp = Blueprint('homeowner_shortlist', __name__)

@homeowner_shortlist_bp.route('/homeowner/shortlist', methods=['GET'])
def view_shortlist():
    if 'user_id' not in session:
        return "Unauthorized", 401
    
    homeowner_id = session['user_id']
    search_query = request.args.get('search', '')
    shortlisted_services = HomeownerShortlistController.get_shortlisted_services(homeowner_id, search_query)
    
    return render_template('homeowner_shortlist.html', services=shortlisted_services, search=search_query)