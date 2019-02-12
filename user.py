class User:
    """
    Class that generates new instances of User
    """

    pass
    user_list = [] 
    def __init__(self,first_name,last_name,phone_number,email):

        # '''
        # __init__ method that helps us define properties for our objects.

        # Args:
        #     first_name: New contact first name.
        #     last_name : New contact last name.
        #     number: New contact phone number.
        #     email : New contact email address.
        # '''
        # docstring removed for simplicity
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

       # Empty contact list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

        