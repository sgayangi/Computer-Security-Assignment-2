import hashlib
class User:
    def __init__(self, id, username: str, password: str, userType: str, permissions: str):
        """
        Create a new user
        @param userType: 1 for Doctor, 2 for Nurse, 3 for LabAssistant, 4 for Patient
        @param permissions: two bits, first for read, second for write, both 0 means no access
        """
        self.id = id
        self.username = username
        self.password = password
        userTypes = ["Admin", "Doctor", "Nurse", "Lab Assistant", "Patient"]
        self.role = userTypes[userTypes.index(userType)]
        self.userType = userType 
        print(self.userType)
        # permissionType = ["read", "read write", "no permission"]
        self.permissions = permissions
        if (permissions == "read"):
            self.privilege_level = "10"
        elif (permissions == "write"):
            self.privilege_level = "11"
        self.access_string = self.privilege_level+"000000"
# doctor
# nurse
# lab assistant
# patient
