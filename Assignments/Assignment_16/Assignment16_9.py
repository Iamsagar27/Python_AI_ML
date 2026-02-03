# 9. Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20

def PrintEven():
    evennumbers = ""
   
    for i in range(1, 11):
        evennumbers += str(i*2) + " " 
        
    return evennumbers
        
def main():
    result = PrintEven()
       
    print(result)

if __name__ == "__main__":
    main()
