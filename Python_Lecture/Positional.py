def Display(A, B, C, D):
    print(A, B, C, D)

def main():
    Display(10, 20)               # Not Allowed - TypeError: Display() missing 2 required positional arguments: 'C' and 'D'
    #Display(10, 20, 30, 40, 50)    Not Allowed - More Arguments
    #Display(10,20,30,40)            # Allowed

if __name__ == "__main__":
    main()