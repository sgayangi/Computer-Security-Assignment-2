from user import User
from patient_information import PatientInformation
class Patient:
    # Patients can only access their files

    @staticmethod
    def start(user: User):
        x = input("""What would you like to do?
1: View Drug Prescriptions
2: View Personal Details
3: View Sick Details
4: View Lab Test Prescriptions
5. Edit Personal Details\n""").strip()
        if not PatientInformation.isInvalidFileType(x):
            if not user.hasReadAccess():
                print("Insufficient permissions")
            else:
                PatientInformation.readPatientFile(user.id, x)
        elif (x == "5"):
            data = input("Input personal information: ")
            PatientInformation.updatePatientFile("2", user.id, data)
        else:
            print("Invalid input")
            return
