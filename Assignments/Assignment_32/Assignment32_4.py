# 4. Design automation script which accept directory name and delete all duplicate files from that directory. 
# Write names of duplicate files from that directory into log file named as Log.txt.
# Log.txt file should be created into current directory. Display execution time required for thescript.
# Usage : DirectoryDusplicateRemoval.py “Demo”
# Demo is name of directory.

import sys
import os
import time
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def CheckDuplicateFiles(DirectoryName):
    
    if os.path.exists(DirectoryName) == False:
        print("There is no such directory")
        return

    if os.path.isdir(DirectoryName) == False:
        print("It is not a directory")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            CheckSum = CalculateChecksum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else :
                Duplicate[CheckSum] = [fname]

    return Duplicate

def DeleteDuplicateFiles(DirectoryName):
    Border = "-"*55
    timestamp = time.ctime()
    start_time = time.time()

    SrciptFile = "Assignment32_4_%s.log" %(timestamp)
    SrciptFile = SrciptFile.replace(" ","_")
    SrciptFile = SrciptFile.replace(":","_")
    
    ScriptFileObj = open(SrciptFile,"w")
    ScriptFileObj.write(Border+"\n")
    ScriptFileObj.write("--------------- Python Automation Script --------------"+"\n")
    ScriptFileObj.write(Border+"\n")
    ScriptFileObj.write("\n")

    duplicate = CheckDuplicateFiles(DirectoryName)
    Result = list(filter(lambda x : len(x) > 1, duplicate.values()))

    Count = 0
    DeleteCount = 0
    for value in Result:
        ScriptFileObj.write("Duplicate Files are :" + "\n")
        for subvalue in value:
            ScriptFileObj.write(subvalue + "\n")
            Count += 1
            if Count > 1:
                os.remove(subvalue)
                DeleteCount += 1
        Count = 0
    
    ScriptFileObj.write("\n")
    ScriptFileObj.write(f"Total Duplicate files deleted : {DeleteCount}" +"\n")
    
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
        DeleteDuplicateFiles(sys.argv[1])
    else :
        print("Invalid number of arguments")
        print("1st argument : Directory Name")

if __name__ == "__main__":
    main()