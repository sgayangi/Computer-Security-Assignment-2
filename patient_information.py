from utilities import Utilities


class PatientInformation:

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
    def readDrugFile(patientID: str):
        print("=================================")
        print("Drug Details for Patient ID " + patientID)
        print("=================================")
        print(Utilities.returnPatientData(
            "patient information/drug prescriptions/"+patientID+".txt"))
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

    @staticmethod
    def updatePatientFile(file_type: str, patientID: str ,data:str):
        if (file_type == "1"):
            PatientInformation.updateDrugFile(patientID, data)
        elif (file_type == "2"):
            PatientInformation.updateLabFile(patientID, data)
        elif (file_type == "3"):
            PatientInformation.updatePersonalFile(patientID, data)
        elif (file_type == "4"):
            PatientInformation.updateSicknessFile(patientID, data)
        else:
            print("Invalid file type")

    @staticmethod
    def updateDrugFile(patientID: str, data:str):
        Utilities.updatePatientData(
            "patient information/drug prescriptions/"+patientID+".txt", data)

    @staticmethod
    def updateLabFile(patientID: str, data: str):
        
        Utilities.updatePatientData(
            "patient information/lab test prescriptions/"+patientID+".txt", data)
        

    @staticmethod
    def updatePersonalFile(patientID: str, data: str):
        Utilities.updatePatientData(
            "patient information/personal details/"+patientID+".txt", data)

    @staticmethod
    def updateSicknessFile(patientID: str, data: str):
        Utilities.updatePatientData(
            "patient information/sickness details/"+patientID+".txt", data)
