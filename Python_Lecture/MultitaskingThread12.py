import time
import threading

def SumEven(No):
    Sum = 0

    for i in range(2, No + 1, 2):
        Sum = Sum + i

    print("Sum of even numbers :", Sum)

def SumOdd(No):
    Sum = 0

    for i in range(1, No + 1, 2):
        Sum = Sum + i

    print("Sum of odd numbers :", Sum)

def main():
    start_time = time.time()
    
    t1 = threading.Thread(target=SumEven , args=(100000000,))
    t2 = threading.Thread(target=SumOdd , args=(100000000,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    end_time = time.time()

    print("Time for execution :", end_time - start_time)

if __name__ == "__main__":
    main()