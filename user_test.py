import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user= User("Cecile","Nyirahabineza","0728236949","habcecile@gmail.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Cecile")
        self.assertEqual(self.new_user.last_name,"Nyirahabineza")
        self.assertEqual(self.new_user.phone_number,"0728236949")
        self.assertEqual(self.new_user.email,"habcecile@gmail.com")


    def test_save_user(self):
        '''
        test_save_user test case to test if the contact object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),3)

# Items up here...

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0728236949",".habcecile") # new user
            test_user.save_use()
            self.assertEqual(len(User.user_list),2)

            # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            # test_user.user_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0712345678","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

            # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            # User.user_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0712345678","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

            # More tests above
    def test_delete_user(self):
            '''
            test_delete_contact to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0728236949","habcecile@gmail.com") # new contact
            test_user.save_user()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(User.user_list),1)
            def delete_user(self):
            '''
            delete_user method deletes a saved user from the user_list
            '''
         # user.user_list.remove(self)         
if __name__ == '__main__':
    unittest.main()
