from utilities import Utilities

class PatientInformation:
    
    @staticmethod
    def readDrugFile(patientID: str):
        print("=================================")
        print("Drug Details for Patient ID " + patientID)
        print("=================================")
        print(Utilities.returnPatientData("patient information/drug prescriptions/"+patientID+".txt"))
        print("=================================")
        print()

    @staticmethod
    def readLabFile(patientID: str):
        print("=================================")
        print("Lab Details for Patient ID " + patientID)
        print("=================================")
        print(Utilities.returnPatientData(
            "patient information/lab test prescriptions/"+patientID+".txt"))
        print("=================================")
        print()

    @staticmethod
    def readPersonalFile(patientID: str):
        print("=================================")
        print("Personal Details for Patient ID " + patientID)
        print("=================================")
        print(Utilities.returnPatientData(
            "patient information/personal details/"+patientID+".txt"))
        print("=================================")
        print()

    @staticmethod
    def readSicknessFile(patientID: str):
        print("=================================")
        print("Sickness Details for Patient ID " + patientID)
        print("=================================")
        print(Utilities.returnPatientData(
            "patient information/sickness details/"+patientID+".txt"))
        print("=================================")
        print()


