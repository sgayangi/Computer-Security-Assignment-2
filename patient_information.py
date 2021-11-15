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
    def readLabFile(patientID: str): pass

    @staticmethod
    def readPersonalFile(patientID: str): pass

    @staticmethod
    def readSicknessile(patientID: str): pass


