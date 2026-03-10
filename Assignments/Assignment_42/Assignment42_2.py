# 2. Using the same dataset from above question, calculate model performance.
# Tasks
# 1. Predict all Y values using regression equation.
# 2. Calculate:
# Mean Squared Error (MSE)
# R2 Score
# Show all intermediate calculations.

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def CalculateMean(list):
    summation = 0
    for i in list:
        summation += i

    return summation/len(list)

def SimpleLinearRegression():
    Border = "-"*50
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print(Border)
    print("Independent Variable : X - ", X)
    print("Dependent Variable : Y - ", Y)

    # Mean of X (X)
    X_mean = CalculateMean(X)

    # Mean of Y (Y)
    Y_mean = CalculateMean(Y)

    print(Border)
    print("X_Mean : ", X_mean)
    print("Y_Mean : ", Y_mean)
    print(Border)

    # Slope (m)
    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator = numerator + ((X[i] - X_mean) * (Y[i] - Y_mean))
        denominator = denominator + ((X[i] - X_mean) ** 2)

    m = numerator/denominator

    print("Slope of line (m) :", m)
    print(Border)

    # Intercept (c)
    # Y = mx + c
    # c = Y - mx

    c = Y_mean - (m * X_mean)
    print("Slope Intercept (c) : ", c)
    print(Border)

    print("Predicted Y for X = 6 : ", m * 6 + c)
    print(Border)

    # Predict all Y values using regression equation.
    Y_pred = []

    print("Predicted Y values :")
    for i in range(len(X)):
        y = m*X[i] + c
        Y_pred.append(y)
        print(f"X = {X[i]} , Actual Y = {Y[i]}, Predicted Y = {y}")

    print(Border)
    
    MSE = mean_squared_error(Y, Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y, Y_pred)

    print("Mean Squared Error : ", MSE)
    print("Root Mean Squared Error : ", RMSE)
    print("R square value : ", R2)
    print(Border)

def main():
    SimpleLinearRegression()

if __name__ == "__main__":
    main()