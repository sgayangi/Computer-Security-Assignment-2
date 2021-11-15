from common import Common
from user import User
class Driver:

    @staticmethod
    def main():
        print("What would you like to do?\n1: Login\n2: Register")
        function = input()
        if function =="2": 
            username = input('Username: ')
            password = input('Password: ')
            userType = input(
                'User Type: Select from "Doctor", "Nurse", "Lab Assistant", "Patient" \n')
            permissions = input(
                'Permissions: Select from "read", "write" \n')
            # if ((permissions != "read" or permissions != "write") or (userType != "Doctor" or userType != "Nurse" or userType != "Lab Assistant" or userType != "Patient")):
            #     print("Invalid input")
            #     quit()
            Common.register(username, password, userType, permissions)
            print("Registration successful. Please login.")
        elif function == "1":
            username = input('Username: ')
            password = input('Password: ')
            user = Common.login(username, password)
            print(user.username, user.password, user.userType, user.permissions)
        else:
            print("Invalid input")
            quit()

if __name__ == "__main__":
    Driver.main()
