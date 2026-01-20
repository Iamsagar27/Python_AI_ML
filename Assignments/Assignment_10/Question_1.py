# 1. Write a program which accepts one number and prints multiplication table of that number. 
# Input: 4  
# Output: 4 8 12 16 20 24 28 32 36 40 

def Table(No):
    table = ""
    for i in range(1,11):
        multiple = No * i
        table += str(multiple) + " "

    return table

def main():
    Num = 0
   
    Num = int(input("Enter the number : "))
    Ret = Table(Num)
    print(Ret)
   
if __name__ == "__main__":
    main()