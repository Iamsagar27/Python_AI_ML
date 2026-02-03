# 2. Display File Contents
# Problem Statement : Write a program which accepts a file name from the user, opens that file, and displays the entire
# contents on the console.
# Input : Demo.txt
# Expected Output : Display contents of Demo.txt on console.

import os

def CheckFileExist(FileName):
    Ret = False

    Ret = os.path.exists(FileName)

    if Ret == False :
        print(f"{FileName} file does not exist in current directory")
    else :
        fobj = open(FileName, "r")

        content = fobj.read()
        print(content)

        fobj.close()

def main():
    FileName = input("Enter file name : ")
    if FileName :
        CheckFileExist(FileName)
    else :
        print("File name should not be blank")

if __name__ == "__main__":
    main()