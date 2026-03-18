# 7. Write a Python program using Linear Regression to train a regression model using the dataset below.
# Study Hours       Marks
#       1            50
#       2            55
#       3            60
#       4            65
#       5            70
# Your program should:
# - Train the regression model
# - Print the coefficient
# - Print the intercept

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def LinearRegressionFunction():
    Border = "-"*60

    print(Border)
    X = np.array([1,2,3,4,5]).reshape((-1, 1))
    Y = np.array([50,55,60,65,70])

    print("Values of Independent variables - X : ", X)
    print("Values of Independent variables - Y : ", Y)
    print(Border)

    # Train the model
    model = LinearRegression().fit(X,Y)

    # Coefficient of model
    coefficient = model.coef_
    print("Coefficient : ", coefficient[0])
    print(Border)

    # Intercept of model
    intercept = model.intercept_
    print("Intercept : ", intercept)
    print(Border)

def main():
    LinearRegressionFunction()

if __name__ == "__main__":
    main()
