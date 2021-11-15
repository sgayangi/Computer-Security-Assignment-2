from user import User
import hashlib
import csv
import os
import datetime

class Utilities:

    @staticmethod
    def writeUserToFile(user: User):
        permission = "no permission"
        if (user.privilege_level == "11"): permission = "write"
        elif (user.privilege_level == "10"):
            permission = "read"
        with open('user_details/config.csv', 'a', newline="\n") as fd:
            writer = csv.writer(fd)
            writer.writerow(
                [user.id, user.username, user.password, user.role, permission, int(user.access_string,2)])

    @staticmethod
    def getUserFromCsv(username, password):
        rowFromFile = []
        with open('user_details/config.csv', 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] == username:
                    rowFromFile = row
                    break
        if rowFromFile == []:
            print("Could not find user")
            return False
        else:
            enteredPassword = Utilities.hashPassword(password)
            if enteredPassword == rowFromFile[2]:
                return User(rowFromFile[0], rowFromFile[1], rowFromFile[2], rowFromFile[3], rowFromFile[4])
            else:
                print("Incorrect password. Please try again.")
                return False

    @staticmethod
    def hashPassword(password):
        pw_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return pw_hash

    @staticmethod
    def returnPatientData(file_path:str):
        if not os.path.isfile(file_path):
            return "Requested file does not exist for this patient."
        with open(file_path) as f:
            lines = f.read()
        return lines

    @staticmethod
    def updatePatientData(file_path: str, data: str):
        now = datetime.datetime.now()
        file_object = open(file_path, 'a')
        file_object.write(data+"\n")
        file_object.write("Update done on: " +
                          now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file_object.write("\n")
        file_object.close()