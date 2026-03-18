# 9. Consider the dataset below:
# StudyHours     SleepHours      Marks
#      1             7            50
#      2             6            55
#      3             7            60
#      4             6            65
#      5             8            70

# Write a Python program to:
# - Train a regression model using this dataset
# - Print the coefficients for both features
# - Print the intercept

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def LinearRegressionFunction():
    Border = "-"*75

    print(Border)
    X = [[1,7],[2,6],[3,7],[4,6],[5,8]]
    Y = [50,55,60,65,70]

    print("Values of Independent variables - X : ", X)
    print("Values of Independent variables - Y : ", Y)
    print(Border)

    # Train the model
    model = LinearRegression().fit(X,Y)

    # Coeffiecient of model
    coefficient = model.coef_
    print("Coeffiecient of StudyHours: ", coefficient[0])
    print("Coeffiecient of SleepHours: ", coefficient[1])
    print(Border)

    # Intercept of model
    intercept = model.intercept_
    print("Intercept of model : ", intercept)
    print(Border)

def main():
    LinearRegressionFunction()

if __name__ == "__main__":
    main()