from app.entity.user_account import UserAccount

class LoginController:
    def authenticate_user(self, username, password):
        self.validate_login_input(username, password)
        user = UserAccount.authenticate(username, password)
        if not user:
            raise ValueError("Invalid username or password")
        if user.is_suspended:
            raise ValueError("Your account has been suspended. Please contact the user admins.")
        return user

    def validate_login_input(self, username, password):
        if not username or not password:
            raise ValueError("Both username and password are required")