import threading

iCnt = 0
lobj = threading.Lock()

def Update():
    global iCnt
    
    for _ in range(20000000):
        with lobj:
            iCnt = iCnt + 1
        
def main():
    global iCnt
    
    t1 = threading.Thread(target=Update)
    t2 = threading.Thread(target=Update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Value of iCnt :", iCnt)

if __name__ == "__main__":
    main()