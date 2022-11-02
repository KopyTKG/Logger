from sys import path
import datetime, io, os
 

class logger:
    def __init__(self, filename):
        if filename != "":
            self.filename = f"{filename}-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.log"
        else:
            self.filename = "Error.log"

        self.fullPath = path[0] + "/logs/" + self.filename
        
        self.createFile(self.fullPath)

        self.runtest()
        
    def getpreset(self):
        return f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - " 

    def createFolder(self):
        print_error = ""
        try:
            os.mkdir(path[0]+"/logs/")
        except:
            print_error = "Error: Folder already exists \n"
        return print_error

    def createFile(self, file):
        error = self.createFolder()        
        file = open(file,"w")
        file.write(self.getpreset()+"Logger loaded \n")
        file.close()
        if error:
            file = open(self.fullPath, "a")
            file.write(self.getpreset() +error)
            file.close()
    
    def writestatus(self,type, status):
        if(type == "e"):
             status = "Error: "+status
        else:
            status = "Common: "+status

        file = open(self.fullPath, "a")
        file.write(self.getpreset()+status+"\n")
        file.close()

    def runtest(self):
        if self.filename != "Error.log":
            self.writestatus("",self.fullPath)
            self.writestatus("",self.filename)
        else:
            self.writestatus("e", "Missing path to file")
            self.writestatus("e", "Missing filename")

