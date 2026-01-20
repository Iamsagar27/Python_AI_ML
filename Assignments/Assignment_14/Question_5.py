# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False

def main():
    Num = int(input("Enter a number :"))

    Even = lambda x : True if x % 2 == 0 else False 

    print(Even(Num))

if __name__ == "__main__":
    main()