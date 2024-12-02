class LoginSystem:
    def __init__(self, correct_username, correct_password):
        self.correct_username = correct_username
        self.correct_password = correct_password
        self.max_attempts = 3

    def authenticate(self):
        attempts = 0

        while attempts < self.max_attempts:
            username = input("Enter username: ")
            password = input("Enter password: ")
            retype_password = input("Re-type password: ")
            
            if self._is_valid_credentials(username, password, retype_password):
                print("Login successful!")
                return True
            else:
                print("Incorrect credentials or passwords do not match. Try again.")
                attempts += 1
        
        print("Too many failed attempts. Account locked.")
        return False

    def _is_valid_credentials(self, username, password, retype_password):
        return (
            username == self.correct_username and
            password == self.correct_password and
            password == retype_password
        )


if __name__ == "__main__":
    login_system = LoginSystem(correct_username="user", correct_password="pass")
    login_system.authenticate()
