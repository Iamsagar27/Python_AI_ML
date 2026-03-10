# 1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm. 
# The algorithm should be implemented manually without using any machine learning library.
# The program should:
# Calculate Euclidean distance
# Sort distances
# Select K nearest neighbors
# Predict the class based on majority voting

# Dataset :
# Point     X        Y        Label
# A         1        2         Red
# B         2        3         Red
# C         3        1         Blue
# D         6        5         BLue

# Tasks
# 1. Accept X and Y coordinates of a new point from the user.
# 2. Compute Euclidean distance from all dataset points.
# 3. Sort the distances.
# 4. Select K = 3 nearest neighbors.
# 5. Predict the class label.

# Input Format :
# Enter X coordinate: 2
# Enter Y coordinate: 2

# Expected Output:
# Nearest Neighbors:
# A Distance: 1.0
# B Distance: 1.0
# C Distance: 1.41

# Predicted Class: Red

import numpy as np
import math

def EuclideanDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def MarvellousKNeighborsClassifier():
    border = "-"*40

    data = [
        {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
        {'point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
        {'point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
        {'point' : 'D', 'X' : 5, 'Y' : 6, 'label' : 'Blue'}
    ]

    print(border)
    print("UserDefined KNN")
    print(border)

    print(border)
    print("Training Data Set")
    print(border)

    for i in data:
        print(i)

    print(border)

    # Accept X and Y coordinates of a new point from the user.
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    new_point = {'X': x, 'Y': y}

    # Compute Euclidean distance from all dataset points.
    for d in data:
        d['distance'] = EuclideanDistance(d,new_point)

    print(border)
    print("Calculated distances are : ")
    print(border)

    for d in data:
        print(d)

    sorted_data = sorted(data, key= lambda item : item['distance'])

    print(border)
    # Sort the distances.
    print("Sorted data is : ")
    print(border)

    for d in sorted_data:
        print(d)

    k = 3
    nearest = sorted_data[:k]

    print(border)
    # Select K = 3 nearest neighbors.
    print("Nearest 3 elements are : ")
    print(border)

    for d in nearest:
        print(d)

    # Voting
    votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0) + 1

    print(border)
    #Predict the class based on majority voting
    print("Voting result is : ")
    print(border)

    for d in votes:
        print("Name : ",d, "Number of votes : ",votes[d])

    print(border)

    predicted_class = max(votes, key=votes.get)

    print("Predicted class of (3,3) is : ",predicted_class)

def main():
    MarvellousKNeighborsClassifier()

if __name__ == "__main__":
    main()