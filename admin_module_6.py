class User:
    """creates a user profile"""
    def __init__(self,first_name,last_name,phone,address,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.login_attempts = login_attempts

    def describe_user(self):
        """prints user info"""
        print(f'User Info\n{self.first_name}\n{self.last_name}\n{self.phone}\n{self.address}\n{self.login_attempts}')

    def set_login_attempts(self, logins):
        """increases login attempts"""
        self.login_attempts += logins
    def reset_logins(self):
        """resets logins to zero"""
        self.login_attempts = 0
class Admin:
    def __init__(self,privelages):
        self.privleges = privelages

class Privleges:
    def __init__(self,privelages):
        self.privleges = privelages

    def show_privelages(self):
        """prints privelages"""
        print(self.privleges)