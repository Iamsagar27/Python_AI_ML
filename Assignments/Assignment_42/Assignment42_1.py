# 1. Implement Simple Linear Regression manually without using any ML. library.
# Dataset
# X = [1, 2, 3, 4, 5]
# Y = [3, 4, 2, 4, 5]
# Tasks
# Calculate:
# 1. Mean of X (X)
# 2. Mean of Y (Y)
# 3. Slope (m)
# 4. Intercept (c)
# Expected Output Example
# Mean of x = 3 
# Mean of Y = 3.6
# Slope  (m) = 0.4
# Intercept (c) = 2.4
# Regression Equation: Y = 0.4X + 2.4
# Predicted Y for X = 6 : 4.8

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

    X = 6
    Y = m * X + c
    print("Predicted Y for X = 6 : ", Y)
    print(Border)

def main():
    SimpleLinearRegression()

if __name__ == "__main__":
    main()