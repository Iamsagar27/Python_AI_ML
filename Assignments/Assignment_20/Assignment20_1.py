# 1. Design a Python application that creates two separate threads named Even and Odd.
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module.
# • Ensure proper thread creation and execution.

import threading

def Even():
    even = ""
    count = 10
    num = 2
    while count != 0:
        # "" = "" + 2 + " "
        # 2 = 2 + 2 + " "
        even = even + str(num) + " "
        num +=2
        count -=1

    print(even)


def Odd():
    odd = ""
    count = 10
    num = 1
    while count != 0:
        odd = odd + str(num) + " "
        num +=2
        count -=1

    print(odd)

def main():
    EvenThread = threading.Thread(target=Even)
    OddThread = threading.Thread(target=Odd)

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()

if __name__ == "__main__":
    main()