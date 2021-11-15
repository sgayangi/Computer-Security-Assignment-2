from user import User
import hashlib
import csv
import os

class Utilities:

    @staticmethod
    def writeUserToFile(user: User):
        # userTypes = ["Admin", "Doctor", "Nurse", "Lab Assistant", "Patient"]
        # permissionType = ["read", "read write", "no permission"]
        # so 00 means no permission
        permission = "no permission"
        if (user.privilege_level == "11"): permission = "read write"
        elif (user.privilege_level == "10"):
            permission = "read"
        
        with open('user_details/config.csv', 'a', newline="\n") as fd:
            writer = csv.writer(fd)
            writer.writerow(
                [user.username, user.password, user.role, permission])

    @staticmethod
    def getUserFromCsv(username, password):
        rowFromFile = []
        with open('user_details/config.csv', 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                if row[0] == username:
                    rowFromFile = row
        if rowFromFile == []:
            print("Could not find user")
            quit() 
        else:
            enteredPassword = Utilities.hashPassword(password)
            if enteredPassword == rowFromFile[1]:
                return User(rowFromFile[0], rowFromFile[1], rowFromFile[2], rowFromFile[3])
            else:
                print("Incorrect password. Please try again.")
                quit()

    @staticmethod
    def hashPassword(password):
        pw_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return pw_hash

    @staticmethod
    def returnPatientData(file_path):
        if not os.path.isfile(file_path):
            lines = "File does not exist."
        with open(file_path) as f:
            lines = f.read()
        return lines