# 6. Write a lambda function which accepts one number and returns True if number is odd otherwise False

def main():
    Num = int(input("Enter a number :"))

    Odd = lambda x : True if x % 2 == 1 else False 

    print(Odd(Num))

if __name__ == "__main__":
    main()