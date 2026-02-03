# 2. Count Words in a File
# Problem Statement : Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input : Demo.txt
# Expected Output : Total number of words in Demo.txt.

import os

def CountWords(FileName):
    Ret = False

    Ret = os.path.exists(FileName)

    if Ret == False:
        print("There is no such file")
    else :
        fobj = open(FileName, "r")
        content = fobj.read()

        FileWords = content.split(" ")

        print(f"Total number of words in {FileName} : {len(FileWords)}")

        fobj.close()

def main():
    FileName = input("Enter the name of file : ")

    if FileName:
        CountWords(FileName)
    else :
        print("Please enter file name")

if __name__ == "__main__":
    main()