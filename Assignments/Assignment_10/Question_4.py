# 4. Write a program which accepts one number and prints all even numbers till that number. 
# Input: 10 
# Output: 2 4 6 8 10 

def EvenNumbers(No):
    Even = ""
    for No in range(2,No + 1, 2):
        Even += str(No) + " "
    return Even

def main():
    Num = 0
    Num = int(input("Enter the number :"))
    Ret = EvenNumbers(Num)
    print(Ret)

if __name__ == "__main__":
    main()