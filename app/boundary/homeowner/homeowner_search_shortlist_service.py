from flask import render_template, request, session, redirect, url_for, flash
from app.controller.homeowner.homeowner_search_shortlist_service_controller import HomeownerSearchShortlistController

class HomeownerSearchShortlistService:
    @staticmethod
    def search_shortlist():
        if 'user_id' not in session or session.get('user_type') != 'HomeOwner':
            flash('Please log in as a homeowner to view your shortlist.', 'error')
            return redirect(url_for('login'))
        
        keyword = request.args.get('keyword', '').strip()
        results = HomeownerSearchShortlistController.search_shortlist(session['user_id'], keyword)
        return render_template('homeowner_shortlist_results.html', services=results, keyword=keyword)