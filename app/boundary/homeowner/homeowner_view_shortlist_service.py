from flask import render_template, session, redirect, url_for, flash
from app.controller.homeowner.homeowner_view_shortlist_service_controller import HomeownerViewShortlistController

class HomeownerViewShortlistService:
    @staticmethod
    def view_shortlist():
        if 'user_id' not in session or session.get('user_type') != 'HomeOwner':
            flash('Please log in as a homeowner to view your shortlist.', 'error')
            return redirect(url_for('login'))
        
        services = HomeownerViewShortlistController.get_shortlisted_services(session['user_id'])
        return render_template('homeowner_shortlist.html', services=services)