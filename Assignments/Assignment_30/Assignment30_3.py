# 3. Display File Line by Line
# Problem Statement : Write a program which accepts a file name from the user and displays the contents of the file line by
# line on the screen.
# Input : Demo.txt
# Expected Output : Display each line of Demo.txt one by one.

import os

def DisplayLines(FileName):
    Ret = False

    Ret = os.path.exists(FileName)

    if Ret == False:
        print("There is no such file")
    else :
        fobj = open(FileName, "r")
        content = fobj.read()

        FileLines = content.split("\n")

        print("Contents of file line by line : ")
        for line in FileLines:
            print(line)

        fobj.close()

def main():
    FileName = input("Enter the file name : ")

    if FileName :
        DisplayLines(FileName)
    else :
        print("Please enter a file name")

if __name__ == "__main__":
    main()