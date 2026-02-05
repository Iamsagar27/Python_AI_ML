# 1. Design automation script which accept directory name and display checksum of all files.
# Usage : DirectoryChecksum.py “Demo”
# Demo is name of directory.

import sys
import os
import time
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()    

def CheckSumAllFiles(DirectoryName):
    Border = "-"*55
    if os.path.exists(DirectoryName) == False:
        print("There is no such directory")
        return

    if os.path.isdir(DirectoryName) == False:
        print("It is not a directory")
        return
    
    timestamp = time.ctime()
    start_time = time.time()

    SrciptFile = "Assignment32_1_%s.log" %(timestamp)
    SrciptFile = SrciptFile.replace(" ","_")
    SrciptFile = SrciptFile.replace(":","_")
    
    ScriptFileObj = open(SrciptFile,"w")
    ScriptFileObj.write(Border+"\n")
    ScriptFileObj.write("--------------- Python Automation Script --------------"+"\n")
    ScriptFileObj.write(Border+"\n")
    ScriptFileObj.write("\n")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateChecksum(fname)

            ScriptFileObj.write(f"File name : {fname} Checksum : {Checksum}" + "\n")


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
    if len(sys.argv) == 2:
        CheckSumAllFiles(sys.argv[1])
    else :
        print("Invalid number of arguments")
        print("1st argument : Directory Name")

if __name__ == "__main__":
    main()