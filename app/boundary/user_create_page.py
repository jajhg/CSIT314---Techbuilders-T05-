
from flask import render_template, request, flash, redirect, url_for
from app.controller.user_create_controller import UserCreateController

class UserCreatePage:

    def display_create_user_form(self):
        return render_template("user_create.html")

    def create_user_click(self):
        username = request.form.get("username")
        password = request.form.get("password")
        user_type = request.form.get("user_type")
        userID = request.form.get("userID")  # optional, depends on your setup

        try:
            self.validate_user_input(username, password, user_type)
        except ValueError as e:
            flash(str(e))
            return render_template("user_create.html")

        controller = UserCreateController()
        user = controller.create_user_account(userID, username, password, user_type)

        flash(f"User {username} created successfully!")
        return redirect(url_for("home"))

    def validate_user_input(self, username, password, user_type):
        if not username or not password or not user_type:
            raise ValueError("All fields must be filled out")
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
