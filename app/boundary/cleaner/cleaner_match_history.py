from flask import request, session, redirect, url_for, flash, render_template
from datetime import datetime
from app.controller.cleaner.cleaner_match_history_controller import CleanerMatchHistoryController

class CleanerMatchHistory:
    def display(self):
        if 'user_id' not in session or session.get('user_type') != 'Cleaner':
            flash("Please log in as a cleaner", "warning")
            return redirect(url_for('login'))

        text = request.args.get('q', '').strip()
        date_from_str = request.args.get('from')
        date_to_str   = request.args.get('to')
        date_from = datetime.strptime(date_from_str, '%Y-%m-%d') if date_from_str else None
        date_to   = datetime.strptime(date_to_str,   '%Y-%m-%d') if date_to_str   else None

        matches = CleanerMatchHistoryController.list_matches(
            cleaner_id=session['user_id'],
            text=text or None,
            date_from=date_from,
            date_to=date_to
        )

        return render_template(
            'cleaner_match_history.html',
            matches=matches,
            search_text=text,
            date_from_str=date_from_str or '',
            date_to_str=date_to_str or ''
        )