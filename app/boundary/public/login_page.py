from flask import render_template, request, flash, redirect, url_for, session
from app.controller.user.login_controller import LoginController

class LoginPage:
    def display_login_form(self):
        return render_template("login.html")

    def login_user(self):
        username = request.form.get("username")
        password = request.form.get("password")

        controller = LoginController()
        try:
            user = controller.authenticate_user(username, password)
            session['user_id'] = user.id
            session['username'] = user.username
            session['user_type'] = user.profile.user_type
            # Redirect directly to appropriate dashboard based on role
            if user.profile.user_type == 'User Admin':
                return redirect(url_for("admin_dashboard"))
            elif user.profile.user_type == 'Cleaner':
                return redirect(url_for("cleaner_dashboard"))
            elif user.profile.user_type == 'HomeOwner':
                return redirect(url_for("homeowner_dashboard"))
            elif user.profile.user_type == 'Platform Management':
                return redirect(url_for("platform_dashboard"))
            else:
                return redirect(url_for("home"))
            
        except ValueError as e:
            flash(str(e), 'error')
        return render_template("login.html")
    
    def logout_user(self):
        session.clear()
        flash("You have logged out successfully.", 'logout')  # Note the 'logout' category
        return redirect(url_for("home"))