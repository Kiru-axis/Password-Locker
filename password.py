# Cridential class
class Cridential:
    """
    Class that generates new instances of passwords
    """
    password_list = []
# 1. Initialisation
    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password

        
#2. save acount password / save multiple account passwords
    def save_password(self):
        '''
        save_password method saves password objects into password_list
        '''
        Cridential.password_list.append(self)






















# User class 
class User:
    user_list = []
    """
    generates new instances of users to login
    """
    def __init__(self,user,login_password):
        self.user = user
        self.login_password = login_password


