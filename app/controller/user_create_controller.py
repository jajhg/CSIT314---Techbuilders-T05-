from app.entity.user_account import UserAccount

class UserCreateController:
    def validate_user_input(self, username, password, user_type):
        if not username or not password or not user_type:
            raise ValueError("All fields must be filled out")
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")

    def create_user_account(self, userID, username, password, user_type):
        self.validate_user_input(username, password, user_type)

        user = UserAccount(userID, username, password, user_type)
        user.save()  # now saving logic is in Entity
        
        return user

