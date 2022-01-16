
from views.login import Login
from views.registerUser import Register

"""
This is the entry to the whole system
"""
class Client():
    
    """
    The init method creates the connection object to the server that will be used
    throughout the system
    """
    def __init__(self):
        # The connection object to the remote server
        # self.connection = Connection()
        pass

    """
    open() enters the login window with 'None' as the user parameter
    since the user hasn't identified himself and also the connection object
    """
    def open(self):
        login_view = Login(None)
        login_view.show_window()

if __name__ == "__main__":
    c = Client()
    c.open()