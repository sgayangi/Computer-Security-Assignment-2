from user import User
from utilities import Utilities

class Common:

    @staticmethod
    def login(username, password): pass

    @staticmethod
    def register(username: str, password: str, userType: str, permissions: str):
        hashed_password = Utilities.hashPassword(password)
        user = User(username, hashed_password, userType, permissions)
        Utilities.writeUserToFile(user)


