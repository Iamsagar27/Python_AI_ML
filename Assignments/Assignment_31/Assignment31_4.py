# 4. Design automation script which accept two directory names and one file extension.
# Copy all files with the specified extension from first directory into second directory. 
# Second directory should be created at run time.
# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files with extension .exe from Demo to Temp.

import sys
import os
import time

def DirectoryFileCopyPaste(OldDirectoryName, NewDirectoryName, FileExtension):
    Border = "-"*55
    if os.path.exists(OldDirectoryName) == False:
        print("There is no such directory")
        return

    if os.path.isdir(OldDirectoryName) == False:
        print("It is not a directory")
        return
    
    timestamp = time.ctime()
    start_time = time.time()

    SrciptFile = "Assignment31_4_%s.log" %(timestamp)
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
            
        FileCount = 0
        for File in FileName:
            Extension = File.split(".")  
            if Extension[-1] == FileExtension:
                OldFilePath = os.path.join(FolderName, File)
                NewFilePath = os.path.join(NewDirectoryName, File)
                ScriptFileObj.write(f"The file '{File}' is copied from the '{OldDirectoryName}' folder and pasted into the '{NewDirectoryName}' folder.'"+ "\n")
            
                #oObj = open(OldFilePath, "rb")
                #content = oObj.read()
                #nobj = open(NewFilePath, "wb")
                #content = nobj.write(content)

                with open(OldFilePath, "rb") as src:
                    with open(NewFilePath, "wb") as dst:
                        dst.write(src.read())
            else :
                FileCount +=1

        if FileCount == len(FileName):
            ScriptFileObj.write(f"There is no such file whose extension is {FileExtension}")
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
    if(len(sys.argv) == 4):
        DirectoryFileCopyPaste(sys.argv[1],sys.argv[2],sys.argv[3])
    else :
        print("Invalid number of arguments")
        print("1st argument : Old Directory Name")
        print("2nd argument : New Directory Name")
        print("3rd argument : File Extension")

if __name__ == "__main__":
    main()