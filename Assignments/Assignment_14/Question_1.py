# 1. Write a lambda function which accepts one number and returns square of that number 

def main():
    Num = int(input("Enter a number :"))

    Square = lambda x : x ** 2

    print(Square(Num))

if __name__ == "__main__":
    main()