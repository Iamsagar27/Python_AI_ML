# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64

Power = lambda x : 2**x

def main():
    number = int(input("Enter a number : "))
    result = Power(number) 
    print(result)

if __name__ == "__main__":
    main()