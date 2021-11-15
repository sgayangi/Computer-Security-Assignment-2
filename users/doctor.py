from user import User
from patient_information import PatientInformation

class Doctor:
# Doctors can access all 4 types of reports

    @staticmethod
    def start(user: User):
        x = input("""What would you like to do?
1: View Patient File
2: Update/Create Patient File\n""").strip()
        patient_id = input("Input Patient ID: ")
        # personal details, sickness details, drug prescriptions, and lab test prescriptions
        if (x == "1"):
            file_type = input("""Select File Type.
1: Drug Prescriptions
2: Personal Details of Patient
3: Sickness Details
4: Lab Test Prescriptions\n""")
        else:
            file_type = input("""Select File Type.
1: Drug Prescriptions
3: Sickness Details
4: Lab Test Prescriptions\n""")
        if x == "1":
            if (file_type != "1" and file_type != "2" and file_type != "3" and file_type != "4"):
                print("Invalid input")
                return
            if user.privilege_level != "10" and user.privilege_level != "11":
                print("Insufficient permissions")
            else:
                PatientInformation.readPatientFile(patient_id, file_type)
        elif x == "2":
            if (file_type != "1" and file_type != "3" and file_type != "4"):
                print("Invalid input")
                return
            if user.privilege_level != "11":
                print("Insufficient permissions")
            else:
                data = input("Input patient information: ")
                PatientInformation.updatePatientFile(file_type, patient_id, data)
        
        else:
            print("Invalid input")
            return
# ddnnllpp
