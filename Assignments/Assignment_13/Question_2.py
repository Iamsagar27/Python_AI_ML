# 2. Write a program which accepts radius of circle and prints area of circle. 

from math import pi 

def AreaOfCircle(r):
    Area = 0
    Area = pi * (r**2)
    return Area

def main():
    Radius = int(input("Enter the radius:"))

    Result = AreaOfCircle(Radius)

    print("Area of circle : ", Result)

if __name__ == "__main__":
    main()
