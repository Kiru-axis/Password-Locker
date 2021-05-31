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

    









if __name__ == "__main__":
    unittest.main()
