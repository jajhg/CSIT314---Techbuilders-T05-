
from flask import request, session, redirect, url_for, flash
from app.controller.homeowner.homeowner_match_service_controller import HomeownerMatchServiceController

class HomeownerMatchService:
    def confirm_match(self):
        if 'user_id' not in session or session.get('user_type') != 'HomeOwner':
            flash("Login as Homeowner required", "warning")
            return redirect(url_for('login'))

        service_id = request.args.get('service_id')
        if not service_id:
            flash("Missing service ID", "danger")
            return redirect(url_for('homeowner_dashboard'))

        success, message = HomeownerMatchServiceController.create_match(service_id, session['user_id'])
        flash(message, "success" if success else "danger")
        return redirect(url_for('homeowner_dashboard'))  # Or return to service details