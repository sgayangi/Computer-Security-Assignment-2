from utilities import Utilities

class PatientInformation:

    @staticmethod
    def readPatientFile(patientID: str, file_type: str):
        if (file_type == "1"):
            PatientInformation.readDrugFile(patientID)
        elif (file_type == "4"):
            PatientInformation.readLabFile(patientID)
        elif (file_type == "2"):
            PatientInformation.readPersonalFile(patientID)
        elif (file_type == "3"):
            PatientInformation.readSicknessFile(patientID)
        else:
            print("Invalid file type")

    @staticmethod
    def readDrugFile(patientID: str):
        x = Utilities.returnPatientData(
            "patient information/drug prescriptions/" + patientID + ".txt")
        if (x != "Requested file does not exist for this patient."):
            PatientInformation.printUserInformation(x, "Drug", patientID)
        else:
            print(x)

    @staticmethod
    def readLabFile(patientID: str):
        x = Utilities.returnPatientData(
            "patient information/lab test prescriptions/" + patientID + ".txt")
        if (x != "Requested file does not exist for this patient."):
            PatientInformation.printUserInformation(x, "Lab", patientID)
        else:
            print(x)
            
    @staticmethod
    def readPersonalFile(patientID: str):
        x = Utilities.returnPatientData(
            "patient information/personal details/" + patientID + ".txt")
        if (x != "Requested file does not exist for this patient."):
            PatientInformation.printUserInformation(x, "Personal", patientID)
        else:
            print(x)

    @staticmethod
    def readSicknessFile(patientID: str):
        x = Utilities.returnPatientData(
            "patient information/sickness details/" + patientID + ".txt")
        if (x != "Requested file does not exist for this patient."):
            PatientInformation.printUserInformation(x, "Sickness", patientID)
        else:
            print(x)

    @staticmethod
    def printUserInformation(data, type, patientID):
        print("=================================")
        print(type+ " Details for Patient ID " + patientID)
        print("=================================")
        print(data)
        print("=================================")
        print()


    @staticmethod
    def updatePatientFile(file_type: str, patientID: str ,data:str):
        if (file_type == "1"):
            PatientInformation.updateDrugFile(patientID, data)
        elif (file_type == "4"):
            PatientInformation.updateLabFile(patientID, data)
        elif (file_type == "2"):
            PatientInformation.updatePersonalFile(patientID, data)
        elif (file_type == "3"):
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

    @staticmethod
    def isInvalidFileType(file_type: str):
        return file_type != "1" and file_type !="2" and file_type != "3" and file_type != "4"
