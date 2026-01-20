# 2. Write a program which accepts one number and prints its factors. 
# Input: 12 
# Output: 1 2 3 4 6 12 

def NumFactors(No):
    Ret = ""

    for i in range(1, No+1):
        if(No % i == 0):
            Ret += str(i) + " "
    
    return Ret

def main():
    Num = int(input("Enter a number :"))

    Result = NumFactors(Num)

    print(Result)

if __name__ == "__main__":
    main()