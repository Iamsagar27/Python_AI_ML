# 3. Write a program which accepts one number and checks whether it is perfect number or not. 
# Input: 6 
# Output: Perfect Number 

def PerfectNumber(No):
    Sum = 0

    for i in range(1, No):
        if(No % i == 0):
            Sum = Sum + i        

    return Sum

def main():
    Number = int(input("Enter the Number:"))

    Result = PerfectNumber(Number)

    if(Result == Number) :
        print("Perfect Number")
    else :
        print("Not a Perfect Number")

if __name__ == "__main__":
    main()