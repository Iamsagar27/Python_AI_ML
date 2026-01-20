# 5. Write a lambda function which accepts one number and returns True if divisible by 5

def main():
    Num = int(input("Enter a number :"))

    Divisible = lambda x : True if x % 5 == 0 else False 

    print(Divisible(Num))

if __name__ == "__main__":
    main()