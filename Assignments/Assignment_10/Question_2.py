# 2. Write a program which accepts one number and prints sum of first N natural numbers. 
# Input: 5 
# Output: 15

def SumNatural(No):
    Sum = 0
    Sum = int(No * (No + 1) / 2)
    return Sum

def main():
    Result = 0
    Num = 0
    
    Num = int(input("Enter the number : "))
    Result = SumNatural(Num)
    
    print("Sum of natural number :", Result)
    
if __name__ == "__main__":
    main()