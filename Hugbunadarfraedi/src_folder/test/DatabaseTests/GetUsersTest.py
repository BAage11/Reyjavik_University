import unittest
import sys
import os
sys.path.insert(1,os.getcwd())
from src_folder.app.Database.Database import Database

class TestDatabase(unittest.TestCase):

    def test_getUsers(self):
        db = Database()
        users = db.getUsers()
        user = users['1'].split('/')

        self.assertNotEqual(users, None) #Check if getUsers returns anything at all
        self.assertIsInstance(users, dict) #Testing if getUsers function returns a dict
        self.assertNotIsInstance(users, str) #Not str
        self.assertIsInstance(user[0], str) #Check if it slits successfully and returns str
        self.assertIsInstance(user[1], str) # -||-

if __name__ == "__main__":
    unittest.main()