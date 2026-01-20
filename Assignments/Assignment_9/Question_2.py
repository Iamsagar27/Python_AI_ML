# 2. Write a program which contains one function ChkGreater () that accepts two numbers and prints the greater number. 
# Input: 10 20 
# Output: 20 is greater 

def ChkGreater(No1, No2):
    if No1 > No2:
        return No1
    else :
        return No2
   
def main():
    Result = 0
    Num1 = 0
    Num2 = 0
   
    Num1 = int(input("Enter first number :"))
    Num2 = int(input("Enter second number :"))
   
    Result = ChkGreater(Num1, Num2)
   
    print(Result , "is greater")
   
if __name__ == "__main__":
    main()