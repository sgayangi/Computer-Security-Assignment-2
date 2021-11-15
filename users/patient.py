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
4: View Lab Test Prescriptions\n""").strip()
        if user.privilege_level != "10":
            print("Insufficient permissions")
        else:
            PatientInformation.readPatientFile(user.id, x)
