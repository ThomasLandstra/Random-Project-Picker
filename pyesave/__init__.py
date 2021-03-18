# Imports
import os, json

# Misc Functions
def doesAppDirExist(appName:str):
    return os.path.isdir(os.path.join(os.getenv("APPDATA"), appName))

def doesSaveExist(appName:str, saveName:str, extention:str = "unknown"):
    if extention == "unknown":
        types = ["txt", "dat", "gam", "sav", "tmp", "bak", "cfg", "json"]
        for ext in type:
            dir = os.path.join(os.path.join(os.getenv("APPDATA"), appName), saveName + "." + ext)
            if os.path.isfile(dir):
                return True
    else:
        dir = os.path.join(os.path.join(os.getenv("APPDATA"), appName), saveName + "." + extention)
        if os.path.isfile(dir):
            return True
            
    return False

def doesAnySaveExist(appName:str):
    dir = os.path.join(os.getenv("APPDATA"), appName)
    if os.path.isfile(dir):
        if len(os.listdir(dir)) == 0:
            return False
        else:
            return True
    else:
        return False

def listSavePaths(appName:str):
    returnVar = []
    for name in os.listdir(os.path.join(os.getenv("APPDATA"), appName)):
        returnVar.append(os.path.join(os.getenv("APPDATA"), appName) + "\\" + name)

    return returnVar

def listSaveFiles(appName:str, returnExtentions:bool = False):
    if returnExtentions:
        return os.listdir(os.path.join(os.getenv("APPDATA"), appName))
    else:
        returnList = []
        for item in os.listdir(os.path.join(os.getenv("APPDATA"), appName)):
            returnList.append(item.split(".")[0])
        return returnList

# Create new save
class newSave:
    def __init__(
        self,
        operatingSys: str,
        appName: str = "PyEsave App",
        saveName: str = "PyEsave Save File",
        fileType: str = "txt"
    ):
        self.appName = appName
        self.saveName = saveName
        self.extention = fileType
        self.OS = operatingSys
        self.data = {}
        try:  # Will make directory if it doesn't already exist
            os.mkdir(os.path.join(os.getenv("APPDATA"), self.appName))
        except:
            pass
        self.saveFile = os.path.join(os.path.join(os.getenv("APPDATA"), self.appName), self.saveName + "." + fileType)

    def createSave(self, data: dict):
        jsonType = ["txt", "dat", "gam", "sav", "tmp", "bak", "cfg", "json"]
        if self.extention in jsonType:
            with open(self.saveFile, "w") as write:
                write.write(str(data))

    def loadSave(self):
        jsonType = ["txt", "dat", "gam", "sav", "tmp", "bak", "cfg", "json"]
        if self.extention in jsonType:
            with open(self.saveFile, "r") as readD:
                data = readD.read()
                self.data = json.loads(data.replace("'", '"'))

    def clearLocalData(self):
        self.data = {}

    def deleteFile(self):
        try:
            os.remove(self.saveFile)
        except:
            pass

    def changeData(self, data: dict):
        jsonType = ["txt", "dat", "gam", "sav", "tmp", "bak", "cfg", "json"]
        self.data.update(data)  # Add data to local copy
        if self.extention in jsonType:
            with open(self.saveFile, "w") as write:
                write.write(str(data))

    def removeData(self, data:dict):
        removeList = []
        for x in self.data:
            for y in data:
                if x == y and self.data[x] == data[y]:
                    removeList.append(x)
        
        for x in removeList:
            del self.data[x]