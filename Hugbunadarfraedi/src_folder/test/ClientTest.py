import unittest
import json

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from app.WebSocketClient import MainMenu

from WebSocketClientTests.AddServiceTest import AddServiceTests
from loginTests import TestLogin
from ValidateNewUserRegTest import UserValidation

class TestClient(unittest.TestCase):

    def test_AddServiceTest(self):
        AddServiceTests()
    
    def test_LoginTest(self):
        TestLogin()
    
    def test_UserRegistration(self):
        UserValidation()

if __name__ == "__main__":
    unittest.main()