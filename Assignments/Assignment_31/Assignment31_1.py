# Please follow below rules while designing automation script as
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.

# 1. Design automation script which accept directory name and file extension from user.
# Display all files with that extension.
# Usage : DirectoryFileSearch.py “Demo” “.txt”
# Demo is name of directory and .txt is the extension that we want to search.

import sys
import os
import time

def DirectoryFileSearch(DirectoryName, FileExtension):
    Border = "-"*55
    if os.path.exists(DirectoryName) == False:
        print("There is no such directory")
        return

    if os.path.isdir(DirectoryName) == False:
        print("It is not a directory")
        return
    
    timestamp = time.ctime()
    start_time = time.time()

    SrciptFile = "Assignment31_1_%s.log" %(timestamp)
    SrciptFile = SrciptFile.replace(" ","_")
    SrciptFile = SrciptFile.replace(":","_")

    ScriptFileObj = open(SrciptFile,"w")
    ScriptFileObj.write(Border+"\n")
    ScriptFileObj.write("--------------- Python Automation Script --------------"+"\n")
    ScriptFileObj.write(Border+"\n")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        ScriptFileObj.write(f"Directory Name : {FolderName}"+"\n"+"\n")
        ScriptFileObj.write("")
        ScriptFileObj.write(f"File present in directory '{FolderName}' with '{FileExtension}' extension : "+"\n")
        for fname in FileName:
            Extension = fname.split(".")
            if(Extension[-1] == FileExtension):
                ScriptFileObj.write(fname+"\n")

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
    if len(sys.argv) == 3:
        DirectoryFileSearch(sys.argv[1], sys.argv[2])
    else :
        print("Invalid number of arguments")
        print("1st argument : Directory Name")
        print("2nd argument : File Extension")

if __name__ == "__main__":
    main()