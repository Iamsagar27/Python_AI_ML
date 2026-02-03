# 1. Check File Exists in Current Directory
# Problem Statement : Write a program which accepts a file name from the user and checks whether that file exists in the current
# directory or not.
# Input : Demo.txt
# Expected Output : Display whether Demo.txt exists or not.

import os

def CheckFileExist(FileName):
    Ret = False

    Ret = os.path.exists(FileName)

    if Ret:
        print(f"{FileName} file exist in current directory")
    else :
        print(f"{FileName} file does not exist in current directory")
    

def main():
    FileName = input("Enter file name : ")
    if FileName :
        CheckFileExist(FileName)
    else :
        print("File name should not be blank")

if __name__ == "__main__":
    main()