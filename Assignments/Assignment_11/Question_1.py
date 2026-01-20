# 1. Write a program which accepts one number and checks whether it is prime or not. 
# Input: 11 
# Output: Prime Number 

def CheckPrime(No):
    if (No <= 1):
        return False
    
    for i in range(2, No):
        if(No % i == 0):
            return False
    
    return True

def main():
    Num = int(input("Enter a number :"))

    Ret = CheckPrime(Num)

    if Ret :
        print("Prime Number")
    else :
        print("Not a Prime Number")

if __name__ == "__main__":
    main()