# 2. Design a Python application that creates two threads.
# • Thread 1 should calculate and display the maximum element from an list.
# • Thread 2 should calculate and display the minimum element from the same list.
# • The list should be accepted from the user.

import threading

def Maximum(list):
    max = 0
    for i in list:
        if max < i :
            max = i

    print("Maximum Number from List :", max)


def Minimum(list):
    for i in list:
        min = i
        if min > i :
            min = i

    print("Minimum Number from List :", min)

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    Thread1 = threading.Thread(target=Maximum, args=(numbers,))
    Thread2 = threading.Thread(target=Minimum, args=(numbers,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()
