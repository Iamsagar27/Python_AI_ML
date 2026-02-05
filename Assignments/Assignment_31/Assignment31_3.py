# 3. Design automation script which accept two directory names. Copy all files from first directory
# into second directory. Second directory should be created at run time.
# Usage : DirectoryCopy.py “Demo” “Temp”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files from Demo to Temp.

import sys
import os
import time

def DirectoryFileCopyPaste(OldDirectoryName, NewDirectoryName):
    Border = "-"*55
    if os.path.exists(OldDirectoryName) == False:
        print("There is no such directory")
        return

    if os.path.isdir(OldDirectoryName) == False:
        print("It is not a directory")
        return
    
    timestamp = time.ctime()
    start_time = time.time()

    SrciptFile = "Assignment31_3_%s.log" %(timestamp)
    SrciptFile = SrciptFile.replace(" ","_")
    SrciptFile = SrciptFile.replace(":","_")

    ScriptFileObj = open(SrciptFile,"w")
    ScriptFileObj.write(Border+"\n")
    ScriptFileObj.write("--------------- Python Automation Script --------------"+"\n")
    ScriptFileObj.write(Border+"\n")

    for FolderName, SubFolderName, FileName in os.walk(OldDirectoryName):
        if not os.path.exists(NewDirectoryName):
            os.mkdir(NewDirectoryName)
            ScriptFileObj.write(f"New Directory named '{NewDirectoryName}' is created"+ "\n")
            ScriptFileObj.write("\n")
        else :
            print(f"Directory with name {NewDirectoryName} already exists")
            return
            

        for File in FileName:
            OldFilePath = os.path.join(FolderName, File)
            NewFilePath = os.path.join(NewDirectoryName, File)
            #ScriptFileObj.write(f"The file '{File}' is copied from the '{OldDirectoryName}' folder and pasted into the '{NewDirectoryName}' folder.'"+ "\n")
            
            #fobj = open(OldFilePath, "r")
            #OldFileContent = fobj.read()
            #nobj = open(NewFilePath, "w")
            #nobj.write(OldFileContent)

            with open(OldFilePath, "rb") as src:
                with open(NewFilePath, "wb") as dst:
                    dst.write(src.read())
                    ScriptFileObj.write(f"The file '{File}' is copied from the '{OldDirectoryName}' folder and pasted into the '{NewDirectoryName}' folder."+ "\n")
                    ScriptFileObj.write("\n")

        break

    end_time = time.time()
    execution_time = end_time - start_time

    ScriptFileObj.write("\n")
    ScriptFileObj.write(Border+"\n")
    ScriptFileObj.write("----------- End of Python Automation Script -----------"+"\n")
    ScriptFileObj.write(f"--- Total time of execution : {execution_time} ---"+"\n")
    ScriptFileObj.write(Border+"\n")

    ScriptFileObj.close()
    print("Script has been executed successfully")
                
def main():
    if(len(sys.argv) == 3):
        DirectoryFileCopyPaste(sys.argv[1],sys.argv[2])
    else :
        print("Invalid number of arguments")
        print("1st argument : Old Directory Name")
        print("2nd argument : New Directory Name")

if __name__ == "__main__" :
    main()