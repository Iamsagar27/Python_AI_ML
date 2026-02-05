# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.
# Usage : DirectoryRename.py “Demo” “.txt” “.doc”
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
# After execution this script each .txt file gets renamed as .doc.

import sys
import os
import time

def DirectoryFileRename(DirectoryName, Extension1, Extension2):
    Border = "-"*55
    if os.path.exists(DirectoryName) == False:
        print("There is no such directory")
        return

    if os.path.isdir(DirectoryName) == False:
        print("It is not a directory")
        return
    
    timestamp = time.ctime()
    start_time = time.time()

    SrciptFile = "Assignment31_2_%s.log" %(timestamp)
    SrciptFile = SrciptFile.replace(" ","_")
    SrciptFile = SrciptFile.replace(":","_")

    ScriptFileObj = open(SrciptFile,"w")
    ScriptFileObj.write(Border+"\n")
    ScriptFileObj.write("--------------- Python Automation Script --------------"+"\n")
    ScriptFileObj.write(Border+"\n")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for fname in FileName:
            FileExtension = fname.split(".")
            # print(FileExtension[-1])
            if FileExtension[-1] == Extension1:
                FileExtension[-1] = Extension2

                NewFileName = ".".join(FileExtension)

                OldFilePath = os.path.join(FolderName, fname)
                NewFilePath = os.path.join(FolderName, NewFileName)

                os.rename(OldFilePath, NewFilePath)
                print(f"File renamed from '{fname}' to '{NewFileName}'")
                ScriptFileObj.write(f"File renamed from '{fname}' to '{NewFileName}'"+ "\n")
            elif FileExtension[-1] == Extension2:
                ScriptFileObj.write("New extension is same as old file extension" + "\n")

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
        DirectoryFileRename(sys.argv[1],sys.argv[2],sys.argv[3])
    else :
        print("Invalid number of arguments")
        print("1st argument : Directory Name")
        print("2nd and 3rd argument : File Extension")

if __name__ == "__main__" :
    main()