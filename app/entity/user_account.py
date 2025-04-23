class UserAccount:
    def __init__(self, userID, username, password, userAccType):
        self.userID = userID
        self.username = username
        self.password = password
        self.userAccType = userAccType

    def save(self):
        # Simulate save logic here
        print(f"Saving user: {self.username}, Role: {self.userAccType}")
