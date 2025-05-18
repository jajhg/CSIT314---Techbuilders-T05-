from werkzeug.security import generate_password_hash
from app.entity.user_account import UserAccount
from app.entity.user_profile import UserProfile
from extensions import db

class UserCreateController:
    def validate_user_input(self, username, password, user_type, fullname, phone, dob, gender):
        # Check all fields are filled
        if not all([username, password, user_type, fullname, phone, dob, gender]):
            raise ValueError("All fields must be filled out")
        
        # Check password length is at least 8 characters long
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        
        # Check phone number length and if it contains only digits
        if len(phone) != 8 or not phone.isdigit():
            raise ValueError("Phone number must be exactly 8 digits and contain only numbers.")
        
        # Check for duplicate username
        if UserAccount.find_by_username(username):
            raise ValueError("Username already exists. Please choose a different username, please try again.")
            
        # Check for duplicate phone number
        if UserAccount.find_by_phone(phone):
            raise ValueError("Phone number already exists. Please choose a different phone number, please try again.")
        
        # Check password cannot be same as username
        if password == username:
            raise ValueError("Password cannot be the same as your username, please try again.")
            
        # Check password cannot be same as phone number
        if password == phone:
            raise ValueError("Password cannot be the same as your phone number, please try again.")
            
        # Check username cannot be same as phone number
        if username == phone:
            raise ValueError("Username cannot be the same as your phone number, please try again.")
            
        # Additional password complexity checks (optional)
        if password.isnumeric():
            raise ValueError("Password must contain letters, not just numbers, please try again.")
            
        if password.lower() == password:
            raise ValueError("Password should contain at least one uppercase letter, please try again")
            
        if not any(char.isdigit() for char in password):
            raise ValueError("Password should contain at least one number, please try again.")

    def create_user_account(self, username, password, user_type, fullname, phone, dob, gender):
        self.validate_user_input(username, password, user_type, fullname, phone, dob, gender)
        
        user = UserAccount(
            username=username,
            password=password,
            fullname=fullname,
            phone=phone,
            date_of_birth=dob,
            gender=gender
        )
        
        user.password = password  # Uses @password.setter which hashes it
        db.session.add(user)
        db.session.flush()  # So we can get user.id
        
        profile = UserProfile(id=user.id, user_type=user_type)
        db.session.add(profile)
        db.session.commit()
        
        return user