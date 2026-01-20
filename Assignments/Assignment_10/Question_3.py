# 3. Write a program which accepts one number and prints factorial of that number. 
# Input: 5 
# Output: 120

def Factorial(No):
    factorial = 1
    if(No == 0):
        factorial = 1
    else :
        for No in range(1, No+1):
            factorial = factorial * No
        return factorial

def main():
    Result = 0
    Num = 0
    
    Num = int(input("Enter the number : "))
    Result = Factorial(Num)
    
    print("Factorial of number :", Result)
    
if __name__ == "__main__":
    main()