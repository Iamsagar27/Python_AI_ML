from functools import reduce

def main():
    print("-"*50)
    Data = [11, 10, 15, 20, 22, 27, 30]
    print("Actual Data :", Data)
    print("-"*50)

    FData = list(filter((lambda No : (No % 2 == 0)), Data))
    print("Data after filter :", FData)
    print("-"*50)

    MData = list(map((lambda No : (No + 1)), FData))
    print("Data after map :", MData)
    print("-"*50)

    RData = reduce((lambda A, B : (A + B)), MData)
    print("Data after reduce :", RData)
    print("-"*50)

if __name__ == "__main__":
    main() 