from common import Common
from user import User
from users.doctor import Doctor
from users.lab import LabAssistant
from users.nurse import Nurse
from users.patient import Patient
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
"""Select a user type. (Enter relevant number)
1: Doctor
2: Nurse
3: Lab Assistant
4: Patient\n""").strip()
                if userType != "4":
                    permissions = input(
                        """Select Permission Level. (Enter relevant number)
1: Read Only
2: Read and Write\n""").strip()
                else:
                    permissions = "1"
                p = {
                    "1": "read",
                    "2": "write"
                }
                u = {
                    "1": "Doctor",
                    "2": "Nurse",
                    "3": "Lab Assistant",
                    "4": "Patient"
                }
                Common.register(username, password, u[userType], p[permissions])
                print("Registration successful. Please login.")
            elif function == "1":
                username = input('Username: ')
                password = input('Password: ')
                user = Common.login(username, password)
                if (user != "No user registered"):
                    while True:
                        if (user.userType == "Doctor"):
                            Doctor.start(user)
                        elif (user.userType == "Lab Assistant"):
                            LabAssistant.start(user)
                        elif (user.userType == "Nurse"):
                            Nurse.start(user)
                        elif (user.userType == "Lab Assistant"):
                            Patient.start(user)
                else:
                    print("Invalid username or password.")
            elif function == "q":
                break
            else:
                print("Invalid input")

if __name__ == "__main__":
    Driver.main()
