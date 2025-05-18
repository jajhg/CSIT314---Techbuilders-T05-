
from flask import redirect, url_for, flash
from app.controller.user.suspend_user_controller import SuspendUserController

class SuspendUserPage:
    def suspend_user(self, user_id):
        if SuspendUserController.suspend_user(user_id):
            flash("User suspended successfully", "success")
        else:
            flash("User not found", "error")
        return redirect(url_for('manage_users'))
    
    def unsuspend_user(self, user_id):
        if SuspendUserController.unsuspend_user(user_id):
            flash("User unsuspended successfully", "success")
        else:
            flash("User not found", "error")
        return redirect(url_for('manage_users'))