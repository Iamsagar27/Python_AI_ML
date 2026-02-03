# 3. Write a program which accept one number from user and return its factorial.
# Input : 5 
# Output : 120

def Factorial(num):
    fact = 1
    if(num == 0):
        return fact
    
    for i in range(1,num+1):
        fact *= i

    return fact


def main():
    number = int(input("Enter a number : "))

    result= Factorial(number)

    print(result)

if __name__ == "__main__":
    main()
