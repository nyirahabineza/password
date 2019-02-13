class credentials:
    """
    Class that generates new instances of credentials
    """
    credential_list = [] 

    def __init__(self, username, password):

      # docstring removed for simplicity

        self.username = username
        self.password = password
    
    # Init method up here
    def save_credential(self):


        credential.credential_list.append(self)