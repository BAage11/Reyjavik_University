import os
import sys
sys.path.insert(1, os.getcwd()) # Add new entry point to python script (avoiding ModuleNotFoundError)
from app.GetValidInfo.ValidateNewUserReg import *


def getRegistrationValidation(username,password,confirmPassword):
    check1 = checkIfValidUsername(username)
    if check1 != "":
        return check1
    check2 = checkIfUserExists(username)
    if check2 != "":
        return check2
    check3 = validateNewPassword(password,confirmPassword)
    if check3 != "":
        return check3
    return ""
