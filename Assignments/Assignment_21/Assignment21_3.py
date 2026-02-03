# 3. Design a Python application where multiple threads update a shared variable.
# • Use a Lock to avoid race conditions.
# • Each thread should increment the shared counter multiple times.
# • Display the final value of the counter after all threads complete execution.

import threading

count = 0
lobj = threading.Lock()

def Increment():
    global count

    for _ in range(1000000):
        with lobj:
            count += 1


def main():
    global count
    Thread1 = threading.Thread(target=Increment)
    Thread2 = threading.Thread(target=Increment)

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Count :", count)

if __name__ == "__main__":
    main()
