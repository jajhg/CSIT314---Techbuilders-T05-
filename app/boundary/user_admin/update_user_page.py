from flask import render_template, redirect, url_for, flash, request
from app.controller.user.update_user_controller import UpdateUserController
from app.entity.user_account import UserAccount

class UpdateUserPage:
    def __init__(self):
        self.controller = UpdateUserController()

    def display_update_form(self, user_id):
        """Display the update user form"""
        user = UserAccount.query.get(user_id)
        if not user:
            flash("User not found", "error")
            return redirect(url_for('manage_users'))
        return render_template("admin_update_users.html", user=user)

    def update_user(self, user_id):
        """Handle user update submission"""
        fullname = request.form.get('fullname')
        phone = request.form.get('phone')
        user_type = request.form.get('UserProfile')  

        try:
            success, message = self.controller.update_user(
                user_id, 
                fullname, 
                phone, 
                user_type
            )
            
            flash(message, "success" if success else "error")
            
            if success:
                return redirect(url_for('manage_users'))
            else:
                # Re-display the form with error if update failed
                return render_template(
                    "admin_update_users.html",
                    user=UserAccount.query.get(user_id),
                    phone_error=message if "phone" in message.lower() else None
                )
                
        except ValueError as e:
            # Handle validation errors specifically
            return render_template(
                "admin_update_users.html",
                user=UserAccount.query.get(user_id),
                phone_error=str(e)
            )