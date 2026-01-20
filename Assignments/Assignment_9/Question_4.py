# 4. Write a program which accepts one number and prints cube of that number.

def NumCube(No):
    Cube = No ** 3
    return Cube

def main():
    Result = 0
    Num = 0
   
    Num = int(input("Enter the number : "))
   
    Result = NumCube(Num)
   
    print("Cube of", Num,":", Result)
   
if __name__ == "__main__":
    main()