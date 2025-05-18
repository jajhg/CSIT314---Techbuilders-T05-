from flask import session, redirect, url_for, flash, render_template
from app.controller.cleaner.cleaner_view_tracking_controller import CleanerViewTrackingController

class CleanerViewTracking:
    def display(self):
        if 'user_id' not in session or session.get('user_type') != 'Cleaner':
            flash("Please log in as a cleaner", "warning")
            return redirect(url_for('login'))

        stats = CleanerViewTrackingController.get_view_counts(session['user_id'])
        return render_template('cleaner_view_tracking.html', stats=stats)