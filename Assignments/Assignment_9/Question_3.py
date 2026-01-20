# 3. Write a program which accepts one number and prints square of that number. 
# Input: 5 
# Output: 25

def NumSquare(No):
    Square = No ** 2
    return Square

def main():
    Result = 0
    Num = 0
   
    Num = int(input("Enter the number : "))
   
    Result = NumSquare(Num)
   
    print("Square of", Num,":", Result)
   
if __name__ == "__main__":
    main()