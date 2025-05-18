from flask import render_template, redirect, url_for, flash
from app.controller.user.view_user_controller import ViewUserController

class ViewUserPage:
    def display_all_users(self):
        """Display all users"""
        users = ViewUserController.get_all_users()
        return render_template("admin_view_users.html", users=users)

    def display_user(self, user_id):
        """Display a single user"""
        user = ViewUserController.get_user_by_id(user_id)
        if not user:
            flash("User not found", "error")
            return redirect(url_for('view_users'))
        return render_template("admin_view_user.html", user=user)