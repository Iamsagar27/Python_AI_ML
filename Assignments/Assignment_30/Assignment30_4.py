# 4. Copy File Contents into Another File
# Problem Statement : Write a program which accepts two file names from the user.
# • First file is an existing file
# • Second file is a new file
# Copy all contents from the first file into the second file.
# Input : ABC.txt Demo.txt
# Expected Output : Contents of ABC.txt copied into Demo.txt.

import os
import sys

def CopyFileContent(FileName1, FileName2):
    Ret1 = False
    Ret2 = False

    Ret1 = os.path.exists(FileName1)
    Ret2 = os.path.exists(FileName2)

    if Ret1 == False and Ret2 == False:
        print("Both file does not exist in current directory")
    elif Ret1 == False:
        print(f"{FileName1} file does not exist in current directory")
    elif Ret2 == False:
        print(f"{FileName2} file does not exist in current directory")
    else :
        fobj = open(FileName1, "r")
        OldContent = fobj.read()

        if len(OldContent) > 0 :
            nobj = open(FileName2, "w")
            nobj.write(OldContent)

            nobj = open(FileName2, "r")
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
    FileName1 = input("Enter first file name : ")
    if len(FileName1) == 0:
        print("File names should not be blank")
        return

    FileName2 = input("Enter second file name : ")
    if len(FileName2) == 0:
        print("File names should not be blank")
        return

    CopyFileContent(FileName1, FileName2)

if __name__ == "__main__":
    main()