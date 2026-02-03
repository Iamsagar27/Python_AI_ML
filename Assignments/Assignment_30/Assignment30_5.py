# 5. Search a Word in File
# Problem Statement : Write a program which accepts a file name and a word from the user and checks whether that word is
# present in the file or not.
# Input : Demo.txt Marvellous
# Expected Output : Display whether the word Marvellous is found in Demo.txt or not.

import os

def SearchWordInFile(FileName, SearchWord):
    Ret = False

    Ret = os.path.exists(FileName)

    if Ret == False:
        print("There is no such file")
    else :
        fobj = open(FileName, "r")
        content = fobj.read()

        count = 0
        FileWords = content.split(" ")

        for word in FileWords:
            if(word == SearchWord):
                count += 1

        if count > 0 :
            print(f"'{SearchWord}' word is present in the file")
        else :
            print(f"'{SearchWord}' word is not present in the file")
        
        fobj.close()

def main():
    FileName = input("Enter the file name : ")
    if len(FileName) == 0 :
        print("Please enter a file name")
        return

    SearchWord = input("Enter a word to search : ")
    NoOfWords = SearchWord.split(" ")
    if len(NoOfWords) != 1 :
        print("Please enter a single word to search")
        return

    SearchWordInFile(FileName, SearchWord)
    

if __name__ == "__main__":
    main()