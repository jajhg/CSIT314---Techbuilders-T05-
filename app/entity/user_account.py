class UserAccount:
    def __init__(self, userID, username, password, userAccType):
        self.userID = userID
        self.username = username
        self.password = password
        self.userAccType = userAccType

    ##def SaveUserDetails(self):
      ##  print(f"Saving user: {self.username}, Role: {self.userAccType}")
        # Here we simulate saving to DB or list


def validate_user_input(username, password, user_type):
   
    if not username or not password or not user_type:
        raise ValueError("All fields must be filled out")
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long")



