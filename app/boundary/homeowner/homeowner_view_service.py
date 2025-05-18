from flask import render_template, redirect, url_for, flash, session
from app.controller.homeowner.homeowner_view_service_controller import HomeownerViewServiceController

class HomeownerViewService:
    @staticmethod
    def display_service_details(service_id):
        if 'user_id' not in session or session.get('user_type') != 'HomeOwner':
            flash('Please login as a homeowner to view services.', 'error')
            return redirect(url_for('login'))
        
        service, cleaner = HomeownerViewServiceController.get_service_details(service_id)
        return render_template('homeowner_view_service.html', service=service, cleaner=cleaner)