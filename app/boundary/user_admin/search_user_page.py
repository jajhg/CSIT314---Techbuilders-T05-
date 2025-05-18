from flask import render_template, request
from app.controller.user.search_user_controller import SearchUserController

class SearchUserPage:
    def display_search_form(self):
        """Display the search form"""
        return render_template("admin_search_users.html")

    def display_search_results(self):
        """Display search results"""
        search_term = request.form.get('search_term', '').strip()
        user_profile = request.form.get('user_profile', '').strip()
        
        users = SearchUserController.search_users(search_term, user_profile)
        
        return render_template("admin_search_users.html",
                            users=users,
                            search_term=search_term,
                            user_profile=user_profile)