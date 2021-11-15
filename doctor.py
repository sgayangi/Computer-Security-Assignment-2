from user import User

class Doctor:

    @staticmethod
    def start(user: User):
        x = input("""
        What would you like to do?
        1: View Patient File\n
        2: Update/Create Patient File
        """).strip()
        patient_id = input("Input Patient ID")
        # personal details, sickness details, drug prescriptions, and lab test prescriptions
        file_type = input("""
        Select File Type.
        1: Personal Details of Patient\n
        2: Sickness Details\n
        3: Drug Prescriptions\n
        4: Lab Test Prescriptions
        """)
        if x == "1":
            if user.privilege_level != "10" or user.privilege_level != "11":
                print("Insufficient permissions")
            else:
                Doctor.readPatientFile(patient_id, file_type)
        else:
            if user.privilege_level != "11":
                print("Insufficient permissions")
            else:
                Doctor.updatePatientFile(patient_id)

    @staticmethod
    def readPatientFile(patientID: str, file_type: str): pass
    
    @staticmethod
    def updatePatientFile(patientID: str): pass
