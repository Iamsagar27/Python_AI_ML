# 3. Consider below task
# 1. Train linear regression model.
# 2. Predict salary for 6 years of experience
# 3. Plot regression line using matplotlib.
# Dataset       
# Experience            Salary
# 2                     25000
# 1                     20000
# 3                     30000
# 4                     35000
# 5                     40000
# Expected Output
# Predicted Salary for 6 Years Experience: ₹45000
# Graph should display:
# - Data points
# - Regression line

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def SimpleLinearRegression():
    Border = "-"*50
    X = [[2],[1],[3],[4],[5]]
    Y = [25000,20000,30000,35000,40000]

    print(Border)
    print("Independent Variable : X - ", X)
    print("Dependent Variable : Y - ", Y)
    print(Border)

    model = LinearRegression()
    model.fit(X,Y)

    Y_pred = model.predict([[6]])

    print("Predicted Salary for 6 Years Experience: ₹", int(Y_pred[0]))
    print(Border)

    plt.scatter(X,Y)
    plt.plot(X, model.predict(X))
    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary")
    plt.title("Salary vs Experience")

    plt.show()

def main():
    SimpleLinearRegression()

if __name__ == "__main__":
    main()