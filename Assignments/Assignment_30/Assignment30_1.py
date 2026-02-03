# 1. Count Lines in a File
# Problem Statement : Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input : Demo.txt
# Expected Output : Total number of lines in Demo.txt.

import os

def DisplayNoOfLines(FileName):
    Ret = False

    Ret = os.path.exists(FileName)

    if Ret == False:
        print("There is no such file")
    else :
        fobj = open(FileName, "r")
        content = fobj.read()

        FileLines = content.split("\n")

        print(f"Total number of lines in {FileName} : {len(FileLines)}")

        fobj.close()

def main():
    FileName = input("Enter the file name : ")

    if FileName :
        DisplayNoOfLines(FileName)
    else :
        print("Please enter a file name")

if __name__ == "__main__":
    main()