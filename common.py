from user import User
from utilities import Utilities

class Common:

    @staticmethod
    def login(username, password):
        # hashed_password = Utilities.hashPassword(password)
        # with open('data.csv', 'rt') as f:
        #     reader = csv.reader(f)
        #     usernames = {r[0]: r for r in reader}
        user = Utilities.getUserFromCsv(username, password)
        return user

    @staticmethod
    def register(username: str, password: str, userType: str, permissions: str):
        hashed_password = Utilities.hashPassword(password)
        user = User(username, hashed_password, userType, permissions)
        Utilities.writeUserToFile(user)


