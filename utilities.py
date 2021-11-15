from user import User
import hashlib
import csv

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
    def hashPassword(password):
        # pw_hash = hashlib.sha256(password).hexdigest()
        return password
