from MarvellousFMR import filterX, mapX, reduceX

CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : (No + 1)
Add = lambda A, B : (A + B)

def main():
    print("-"*50)
    Data = [11, 10, 15, 20, 22, 27, 30]
    print("Actual Data :", Data)
    print("-"*50)

    FData = list(filterX(CheckEven, Data))
    print("Data after filter :", FData)
    print("-"*50)

    MData = list(mapX(Increment, FData))
    print("Data after map :", MData)
    print("-"*50)

    RData = reduceX(Add, MData)
    print("Data after reduce :", RData)
    print("-"*50)

if __name__ == "__main__":
    main() 