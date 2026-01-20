# 5. Write a program which accepts one number and prints all odd numbers till that number. 

def OddNumbers(No):
    Odd = ""
    for No in range(1,No + 1, 2):
        Odd += str(No) + " "
    return Odd

def main():
    Num = 0
    Num = int(input("Enter the number :"))
    Ret = OddNumbers(Num)
    print(Ret)

if __name__ == "__main__":
    main()