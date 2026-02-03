# 4. Compare Two Files (Command Line)
# Problem Statement : Write a program which accepts two file names through command line arguments and compares the contents of
# both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure
# Input (Command Line) : Demo.txt Hello.txt
# Expected Output : Success OR Failure

import os
import sys

def CompareFileContent(FileName1, FileName2):
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
        f1obj = open(FileName1, "r")
        File1Content = f1obj.read()

        f2obj = open(FileName2, "r")
        File2Content = f2obj.read()

        if File1Content == File2Content:
            print("Content of both files are same")
        else :
            print("Content of both files are different")

        f1obj.close()
        f2obj.close()

def main():

    if len(sys.argv) == 3:
        CompareFileContent(sys.argv[1], sys.argv[2])
    else :
        print("Invalid number of arguments")
        print("Please enter 2 file names whose data is to be compared")

if __name__ == "__main__":
    main()