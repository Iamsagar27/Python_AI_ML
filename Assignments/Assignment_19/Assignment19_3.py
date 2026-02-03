# 3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 
# and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

#filterList = lambda x :  x if x >= 70 or x <=90 else None 
def filterList(num):
    if(num >= 70 and num <= 90):
        return num
        
#mapList = lambda x : x + 10
def mapList(num):
    return num + 10

#reduceList = lambda x,y : x*y
def reduceList(num1,num2):
    return num1 * num2

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