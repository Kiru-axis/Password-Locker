import unittest
from password import Cridential
from password import User

# Unittest for cridental
class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the paswords class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_passwords = Cridential("Gmail","Pinky","github55.pie")
        # behaviour for user class
        self.new_user = User("Testt","pass")

# Test one:Initialisation   
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_passwords.account,"Gmail")
        self.assertEqual(self.new_passwords.username,"Pinky")
        self.assertEqual(self.new_passwords.password,"github55.pie")


# Test 2: Saving Accounts in the password.txt file    
    def test_save_password(self):
        '''
        test_save_password test case to test if the Account object is saved into
        the Cridential list
        '''
        self.new_passwords.save_password() #add new account

        self.assertEqual(len(Cridential.password_list),1) #checking if the length of the list changes
    

# Test 2.1: Saving multiple Accounts in the password.txt file

    def test_save_multiple_password(self):
        '''
        test_save_multiple_password to check if we can save multiple Account
        objects to our password_list
        '''
        self.new_passwords.save_password() #add new account

        test_password = Cridential("Github","Venus","gitty")
        test_password.save_password() #save
        self.assertEqual(len(Cridential.password_list),2)

    

    









if __name__ == "__main__":
    unittest.main()
