import unittest
import json

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from app.GetValidInfo.ValidateNewUserReg import *


class UserValidation(unittest.TestCase):
    
    def test_checkIfValidUsername(self):
        # given a valid username, what should be the response?
        # should return an empty string
        self.assertEqual(checkIfValidUsername("Olafur"),"")
        # given a invalid username, what should be the response?
        # should return an error message
        # test for invalid number of characters
        self.assertEqual(checkIfValidUsername("Hal"),"Invalid username: Username must contain at least four characters and 30 max, without numbers.")
        self.assertEqual(checkIfValidUsername("thisIsMoreThanThirtyCharactersAndThatIsInvalid"),"Invalid username: Username must contain at least four characters and 30 max, without numbers.")
        # test for invalid characters
        self.assertEqual(checkIfValidUsername("Hal4"),"Invalid username: Username must contain at least four characters and 30 max, without numbers.")

    def test_checkIfValidPassword(self):
        # Password has to be at least 5 characters and at most 30 characters, and the password has to be confirmed  (password == confirm password)
        self.assertEqual(validateNewPassword("password123", "password123"), True)
        self.assertEqual(validateNewPassword("12345", "12345"), True)
        
        self.assertEqual(validateNewPassword("password123", "123password"), False)
        self.assertEqual(validateNewPassword("1234", "1234"), False)
        self.assertEqual(validateNewPassword("12345123451234512345123451234512345", "12345123451234512345123451234512345"), False)



    def test_checkIfUserExists(self):
        # given a valid username that does not exist within the database, what should be the response?
        # should return an empty string
        self.assertEqual(checkIfUserExists("Olafur"),"")
        # given a valid username that does exist within the database, what should be the response?
        # should return an error message
        self.assertEqual(checkIfUserExists("John"),"Invalid: This user already exists within the database.")
        

if __name__ == "__main__":
	unittest.main()