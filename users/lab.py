from user import User
from patient_information import PatientInformation

class LabAssistant:
# Lab assistants can only access lab test prescriptions
    @staticmethod
    def start(user: User):
        x = input("""What would you like to do?
1: View Patient Lab Test File
2: Update/Create Lab Test File\n""").strip()
        patient_id = input("Input Patient ID: ")
        print(user.privilege_level)
        if x == "1":
            if user.hasReadAccess():
                print("Insufficient permissions")
            else:
                PatientInformation.readPatientFile(patient_id, "4")
        elif x=="2":
            if user.hasWriteAccess():
                print("Insufficient permissions")
            else:
                data = input("Input patient information: ")
                PatientInformation.updatePatientFile(
                    "4", patient_id, data)
        else:
            print("Invalid input")
            return
# ddnnllpp
