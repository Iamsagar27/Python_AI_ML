# 8. Using the regression model created in the previous question, write a Python program to predict marks for 6 study hours and 
# display the predicted value.

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

    # Testing the model
    Y_pred = model.predict([[6]])

    print("Predicted Value : ", Y_pred[0])
    print(Border)

def main():
    LinearRegressionFunction()

if __name__ == "__main__":
    main()