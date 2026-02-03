# 3. Copy File Contents into a New File (Command Line)
# Problem Statement : Write a program which accepts an existing file name through command line arguments, creates a new file
# named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line) : ABC.txt
# Expected Output : Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import os
import sys

def CopyFileContent(FileName):
    Ret = False

    Ret = os.path.exists(FileName)

    if Ret == False :
        print(f"{FileName} file does not exist in current directory")
    else :
        fobj = open(FileName, "r")
        OldContent = fobj.read()

        if len(OldContent) > 0 :
            nobj = open("ABC.txt", "w")
            nobj.write(OldContent)

            nobj = open("ABC.txt", "r")
            NewContent = nobj.read()

            if(len(NewContent) > 0):
                print("Content pasted in file successfully")
            else :
                print("Error in pasting content in file")
            nobj.close()
        else:
            print("There is no content in existing file")

        fobj.close()

def main():
    if len(sys.argv) == 2:
        CopyFileContent(sys.argv[1])
    else :
        print("Invalid number of arguments")
        print("Please enter 1 file name whose data is to be copied")

if __name__ == "__main__":
    main()