import time
import multiprocessing
import os

def SumEven(No):
    print("PID of SumEven :", os.getpid())      # 51
    print("PPID of SumEven :", os.getppid())    # CMD 21
    Sum = 0

    for i in range(2, No + 1, 2):
        Sum = Sum + i

    print("Sum of even numbers :", Sum)

def SumOdd(No):
    print("PID of SumOdd :", os.getpid())       # 101
    print("PPID of SumOdd :", os.getppid())     # CMD 21
    Sum = 0

    for i in range(1, No + 1, 2):
        Sum = Sum + i

    print("Sum of odd numbers :", Sum)

def main():
    print("PID of main :", os.getpid())         # 21
    print("PPID of main :", os.getppid())       # CMD 11
    start_time = time.time()
    
    t1 = multiprocessing.Process(target=SumEven , args=(100000000,))
    t2 = multiprocessing.Process(target=SumOdd , args=(100000000,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    end_time = time.time()

    print("Time for execution :", end_time - start_time)

if __name__ == "__main__":
    main()