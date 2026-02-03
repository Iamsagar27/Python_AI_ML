# 4.Write a program which display 5 times Marvellous on screen.
#Output : Marvellous
# Marvellous
# Marvellous
# Marvellous
# Marvellous

def PrintFunc(str):
    for i in range(5):
        print(str)

def main():
    string = input("Enter a number : ")
       
    PrintFunc(string)

if __name__ == "__main__":
    main()
