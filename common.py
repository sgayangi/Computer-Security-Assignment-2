from user import User
from utilities import Utilities
import random
class Common:

    @staticmethod
    def login(username, password):
        user = Utilities.getUserFromCsv(username, password)
        if (user != False):
            return user
        else:
            return "No user registered"

    @staticmethod
    def register(username: str, password: str, userType: str, permission_value: str):
        if (userType == "Doctor"):
            if (permission_value == "read"):
                permissions = "10000000"
            else:
                permissions = "11000000"
        elif (userType == "Nurse"):
            if (permission_value == "read"):
                    permissions = "00100000"
            else:
                permissions = "00110000"
        elif (userType == "Lab Assistant"):
            if (permission_value == "read"):
                permissions = "00001000"
            else:
                permissions = "00001100"
        elif (userType == "Patient"):
            if (permission_value == "read"):
                permissions = "00000010"
            else:
                permissions = "00000011"
        hashed_password = Utilities.hashPassword(password)
        user = User(random.randint(1, 100000000000), username, hashed_password, userType, permissions, False)
        Utilities.writeUserToFile(user)