from common import Common

class Driver:

    @staticmethod
    def main():
        username = input('Username: ')
        password = input('Password: ')
        userType = input(
            'User Type: Select from "Doctor", "Nurse", "Lab Assistant", "Patient" \n')
        permissions = input(
            'Permissions: Select from "read", "write" \n')
        Common.register(username, password, userType, permissions)

if __name__ == "__main__":
    Driver.main()
