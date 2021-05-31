# Cridential class
class Cridential:
    """
    Class that generates new instances of passwords
    """
    password_list = []

    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password


# User class 
class User:
    user_list = []
    """
    generates new instances of users to login
    """
    def __init__(self,user,login_password):
        self.user = user
        self.login_password = login_password
