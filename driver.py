from common import Common
from user import User
from doctor import Doctor
class Driver:

    @staticmethod
    def main():
        while True:
            print("What would you like to do?\n1: Login\n2: Register\nq: Quit")
            function = input()
            if function =="2": 
                username = input('Username: ').strip()
                password = input('Password: ').strip()
                userType = input(
                    'User Type: Select from "Doctor", "Nurse", "Lab Assistant", "Patient" \n').strip()
                permissions = input(
                    'Permissions: Select from "read", "write" \n').strip()
                # if ((permissions != "read" or permissions != "write") or (userType != "Doctor" or userType != "Nurse" or userType != "Lab Assistant" or userType != "Patient")):
                #     print("Invalid input")
                #     quit()
                Common.register(username, password, userType, permissions)
                print("Registration successful. Please login.")
            elif function == "1":
                username = input('Username: ')
                password = input('Password: ')
                user = Common.login(username, password)
                while True:
                    if (user.userType == "Doctor"):
                        Doctor.start(user)
                                
            elif function == "q":
                break
            else:
                print("Invalid input")
                break

if __name__ == "__main__":
    Driver.main()
