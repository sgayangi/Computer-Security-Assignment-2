import hashlib
class User:
    def __init__(self, id, username: str, password: str, userType: str, access_string: str, registered = True):
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
        # permissionType = ["read", "read write", "no permission"]
        if (registered):
            self.access_string = "{0:b}".format(int(access_string))
        else:
            self.access_string = access_string
        one_count = self.access_string.count("1")
        if (one_count == 1):
            permissions = "read"
        elif one_count == 2:
            permissions = "write"
        if (permissions == "read"):
            self.privilege_level = "10"
        elif (permissions == "write"):
            self.privilege_level = "11"
            
    def hasReadAccess(self):
        return self.privilege_level != "10" and self.privilege_level != "11"

    def hasWriteAccess(self):
        return self.privilege_level != "10" and self.privilege_level != "11"
# doctor
# nurse
# lab assistant
# patient
