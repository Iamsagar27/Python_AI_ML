# 2. Write a program which accepts one number and prints count of digits in that number. 
# Input: 7521 
# Output: 4 

def NumberCount(No):
    nCnt = 0

    while No != 0:
        No = No // 10
        nCnt += 1
    
    return nCnt


def main():
    Num = int(input("Enter a number :"))

    Ret = NumberCount(Num)

    print(Ret)

if __name__ == "__main__":
    main()