# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5 
# Input: 15 
# Output: Divisible by 3 and 5 

def Divisible(No):
    if(No % 3 == 0 and No % 5 == 0):
        return True
    else :
        return False

def main():
    Result = 0
    Num = 0

    Num = int(input("Enter the number : "))
    
    Result = Divisible(Num)

    if(Result):
        print("Divisible by 3 and 5")
    else :
        print("Not Divisible by 3 and 5") 
           
if __name__ == "__main__":
    main()