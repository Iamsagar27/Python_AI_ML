# 4. Write a program which accept one number form user and return addition of its factors.
# Input : 12 
# Output : 16 (1+2+3+4+6)

def FactorialAddition(num):
    addition = 0

    for i in range(1,num):
        if(num % i == 0):
            addition += i
        
    return addition


def main():
    number = int(input("Enter a number : "))

    result= FactorialAddition(number)

    print(result)

if __name__ == "__main__":
    main()
