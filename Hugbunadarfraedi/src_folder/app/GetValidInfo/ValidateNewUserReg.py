import os
import sys

# Add new entry point to python script (avoiding ModuleNotFoundError)
sys.path.insert(1, os.getcwd()) 
from src_folder.app.Database.Database import Database


def validateNewPassword(password, confirmed_password):
    """ Check to see if new user password is valid: 1) That password and confirm password are the same, 2) That password is at least 5 characters """
    return password == confirmed_password and len(password) >= 5 and len(password) <= 30


def checkIfValidUsername(username):
    """ Check to see if username is valid (if valid, return an empty string): 1) That username is at least 4 characters, 2) That username is at most 30 characters, 3) That username only contains characters (not numbers). """
    if len(username) < 4 or len(username) > 30:
        return "Invalid username: Username must contain at least four characters and 30 max, without numbers."
    for x in range(len(username)):
        if username[x].isalpha() == False:
            return "Invalid username: Username must contain at least four characters and 30 max, without numbers."
    return ""


def checkIfUserExists(username):
    """ Check in database if the new user registered already exists. If already registered in database,
    return an error message. If not, an empty string is returned (equaling 'True'). """
    db = Database()
    users = db.getUsers()
    for name, value in users.items():
        if username == name:
            return "Invalid: This user already exists within the database."
    return ""
