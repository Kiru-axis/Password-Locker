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