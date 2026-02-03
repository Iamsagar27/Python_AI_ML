# 5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal
# functions instead of lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62


from functools import reduce

def filterList(num):
    count = 0
    for i in range(1,num+1):
        if(num % i == 0):
            count+= 1
    
    if(count == 2):
        return num
    else :
        return None
        
def mapList(num):
    return num*2

def reduceList(num1,num2):
    if num1 > num2:
        return num1
    else :
        return num2

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    print("Input List :", numbers)

    filterNumbers = list(filter(filterList, numbers))
    print("List after filter :", filterNumbers)

    mapNumbers = list(map(mapList, filterNumbers))
    print("List after map :", mapNumbers)

    reduceNumbers = reduce(reduceList, mapNumbers)
    print("Output of reduce :", reduceNumbers)

if __name__ == "__main__":
    main()