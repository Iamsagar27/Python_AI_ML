# 2. Write a lambda function which accepts one number and returns cube of that number 

def main():
    Num = int(input("Enter a number :"))

    Cube = lambda x : x ** 3

    print(Cube(Num))

if __name__ == "__main__":
    main()