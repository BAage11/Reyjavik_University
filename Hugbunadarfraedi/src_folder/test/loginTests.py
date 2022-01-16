import unittest, json, os, sys
sys.path.insert(1,os.getcwd())
#sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from src_folder.app.Database.Database import Database
from src_folder.app.WebSocketClient import MainMenu


class TestLogin(unittest.TestCase):

    def test_getUsers(self):
        pass
        #db = Database()
        #Checks if getUsers returns a string
        #self.assertIsInstance(db.getUsers(), str)
    
    def test_login(self):
        m = MainMenu()
        result = m.loginUser("John","Hundur")
        # Success Case
        self.assertEqual(m.loginUser("John","Hundur"),"John")
        # Failure case
        self.assertEqual(m.loginUser("invaliduser","validpass"),"Username/Password not Found.")

    def test_logout(self):
        #Success case
        m = MainMenu()
        self.assertEqual(m.logOut(),"User has been logged out")
        

    #TODO Make a test that checks if getUsers returns ALL users, and maybe not just some of them
    #TODO Make a success and fail test for login - Done

if __name__ == "__main__":
	unittest.main()