from flask import render_template, request, flash, redirect, url_for
from app.controller.user.create_user_controller import UserCreateController

class UserCreatePage:
    def display_create_user_form(self):
        return render_template("create_user.html")

    def create_user_click(self):
        username = request.form.get("username")
        password = request.form.get("password")
        user_type = request.form.get("UserProfile") 
        fullname = request.form.get("name") 
        phone = request.form.get("phone") 
        dob = request.form.get("dateOfBirth") 
        gender = request.form.get("gender")  

        controller = UserCreateController()
        
        try:
            user = controller.create_user_account(
                username=username,
                password=password,
                user_type=user_type,
                fullname=fullname,
                phone=phone,
                dob=dob,
                gender=gender
            )
            
            flash(f"A new user has been created!")  # Simplified flash for testing
            return redirect(url_for("home"))
            
        except ValueError as e:
            print("Validation error:", str(e))
            flash(str(e))
            return render_template("create_user.html")