# 5. Frequency of a String in File
# Problem Statement :  Write a program which accepts a file name and one string from the user and returns the frequency
# (count of occurrences) of that string in the file.
# Input : Demo.txt Marvellous
# Expected Output : Count how many times "Marvellous" appears in Demo.txt.

import os
import sys

def CheckFileContent(FileName, Word):
    Ret = False

    Ret = os.path.exists(FileName)

    if Ret == False :
        print(f"{FileName} file does not exist in current directory")
    else :
        fobj = open(FileName, "r")
        content = fobj.read()

        contentList = content.split(" ")
        count = 0
        for string in contentList:
            if(string == Word):
                count += 1

        print(f"Word {Word} exists {count} times in {FileName}")
        fobj.close()

def main():
    if len(sys.argv) == 3:
        CheckFileContent(sys.argv[1], sys.argv[2])
    else :
        print("Invalid number of arguments")
        print("Please enter 2 arguments : ")
        print("1st argument : File name ")
        print("2nd argument : String that is to be checked in that file")

if __name__ == "__main__":
    main()