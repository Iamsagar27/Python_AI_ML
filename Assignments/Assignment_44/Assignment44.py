import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def LinearRegressionFunction(DataPath):
    Border = "-"*60

    # Load the dataset
    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    df = pd.read_csv(DataPath)
    print(df.head())

    print(Border)

    # Clean, Prepare and Manipulate data
    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    print("Data after cleaning the dataset :")
    print(df.head())

    print("Missing values count : \n",df.isnull().sum())

    print(Border)
    
    # Train Data
    print(Border)
    print("Step 3 : Train the data")
    print(Border)

    print("Split dataset into independent & dependent variables")
    print(Border)
    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    print(Border)

    print("Split dataset for training & testing")
    print(Border)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5,random_state=42)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    print(Border)

    # Test the data
    print(Border)
    print("Step 4 : Test the data")
    print(Border)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    # Display predicted and expected 
    print(Border)
    print("Step 5 : Display predicted and expected ")
    print(Border)

    Y_pred = model.predict(X_test)

    Result = pd.DataFrame({
        'Actual Sale' : Y_test.values,
        'Expected Sale' : Y_pred 
    })

    print(Result)

def main():
    LinearRegressionFunction("Advertising.csv")

if __name__ == "__main__":
    main()