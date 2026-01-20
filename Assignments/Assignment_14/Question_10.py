# 10. Write a lambda function which accepts three numbers and returns largest number

def main():
    Num1 = int(input("Enter first number :"))
    Num2 = int(input("Enter second number :"))
    Num3 = int(input("Enter third number :"))

    Largest = lambda x,y,z: x if x > y and x > z else y if y > x and y > z else z 

    print(Largest(Num1,Num2,Num3))

if __name__ == "__main__":
    main()