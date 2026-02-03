# 4. Design a Python application that creates three threads named Small, Capital, and Digits.
# • All threads should accept a string as input.
# • The Small thread should count and display the number of lowercase characters.
# • The Capital thread should count and display the number of uppercase characters.
# • The Digits thread should count and display the number of numeric digits.
# • Each thread must also display:
# ◦ Thread ID
# ◦ Thread Name

import threading

def Small(str):
    print("Thread Id of Small :", threading.get_ident())
    print("Thread Name of Small :", threading.current_thread().name)
    smallCount = 0

    for s in  str:
        if s.islower():
            smallCount += 1

    print("Number of small letters :", smallCount)
    


def Capital(str):
    print("Thread Id of Capital :", threading.get_ident())
    print("Thread Name of Capital :", threading.current_thread().name)
    capitalCount = 0

    for s in  str:
        if s.isupper():
            capitalCount += 1

    print("Number of capital letters :", capitalCount)

def Digits(str):
    print("Thread Id of Digits :", threading.get_ident())
    print("Thread Name of Digits :", threading.current_thread().name)
    digitsCount = 0

    for s in  str:
        if s.isdigit():
            digitsCount += 1

    print("Number of digits :", digitsCount)


def main():
    string = input("Enter string : ")

    SmallThread = threading.Thread(target=Small, args=(string,))
    CapitalThread = threading.Thread(target=Capital, args=(string,))
    DigitsThread = threading.Thread(target=Digits, args=(string,))

    SmallThread.start()
    CapitalThread.start()
    DigitsThread.start()

    SmallThread.join()
    CapitalThread.join()
    DigitsThread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()