from flask import render_template, redirect, url_for
from app.entity.user_account import UserAccount

def DisplayCreateUserForm():
    return render_template("user_create.html")

def CreateUserClick(username, password):
    if not username or not password:
        return "Username and Password are required!"  

    
    user = UserAccount(username, password)  
    user.save_user_details()  
    return f"User {username} created successfully!"
