
from app.entity.user_account import UserAccount
def create_user_account(username, password, user_type):

    user = UserAccount(username=username, password=password, user_type=user_type)
    user.save_user_details()  
    return user

def validate_user_input(username, password, user_type):
   
    if not username or not password or not user_type:
        raise ValueError("All fields must be filled out")
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long")

