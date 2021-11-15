from user import User
from patient_information import PatientInformation
class Doctor:
# Doctors can access all 4 types of reports
    @staticmethod
    def start(user: User):
        x = input("""What would you like to do?
1: View Patient File\n
2: Update/Create Patient File\n""").strip()
        patient_id = input("Input Patient ID: ")
        # personal details, sickness details, drug prescriptions, and lab test prescriptions
        file_type = input("""Select File Type.
1: Drug Prescriptions\n
2: Lab Test Prescriptions\n
3: Personal Details of Patient\n
4: Sickness Details\n""")
        print(user.privilege_level)
        if x == "1":
            if user.privilege_level != "10" and user.privilege_level != "11":
                print("Insufficient permissions")
            else:
                Doctor.readPatientFile(patient_id, file_type)
        else:
            if user.privilege_level != "11":
                print("Insufficient permissions")
            else:
                Doctor.updatePatientFile(patient_id)

    @staticmethod
    def readPatientFile(patientID: str, file_type: str):
        if (file_type == "1"):
            PatientInformation.readDrugFile(patientID)
        elif (file_type == "2"):
            PatientInformation.readLabFile(patientID)
        elif (file_type == "3"):
            PatientInformation.readPersonalFile(patientID)
        elif (file_type == "4"):
            PatientInformation.readSicknessFile(patientID)
        else:
            print("Invalid file type")
    
    @staticmethod
    def updatePatientFile(patientID: str): pass
