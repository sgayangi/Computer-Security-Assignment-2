from user import User
from patient_information import PatientInformation

class Nurse:
    # Nurses can only access drug prescriptions, personal details and sickness details
    @staticmethod
    def start(user: User):
        x = input("""What would you like to do?
1: View Patient File
2: Update / Create Patient File\n""").strip()
        if (x=="2"):
            patient_id = input("Input Patient ID: ")
            file_type = input("""Select File Type.
1: Drug Prescriptions
3: Sickness Details\n""")
        elif x=="1":
            patient_id = input("Input Patient ID: ")
            file_type = input("""Select File Type.
1: Drug Prescriptions
2: Personal Details of Patient
3: Sickness Details\n""")
        else:
            print("Invalid input")
            return
        if x == "1":
            if user.hasReadAccess():
                print("Insufficient permissions")
                return
            else:
                PatientInformation.readPatientFile(patient_id, file_type)
        elif x=="2":
            if user.hasWriteAccess():
                print("Insufficient permissions")
                return

            else:
                data = input("Input patient information: ")
                PatientInformation.updatePatientFile(
                    file_type, patient_id, data)
        else:
            print("Invalid input.")
            return


# ddnnllpp
