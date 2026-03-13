import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def KNNFunction(DataPath):
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
    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    print(Border)

    print("Split dataset for training & testing")
    print(Border)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=42)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print(Border)

    # Test the data
    print(Border)
    print("Step 4 : Test the data")
    print(Border)

    model = KNeighborsClassifier(n_neighbors = 3)
    model.fit(X_train_scaled, Y_train)

    # Claculate accuracy
    print(Border)
    print("Step 5 : Accuracy of model")
    print(Border)

    Y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy : ", accuracy*100)
    print(Border)

def main():
    KNNFunction("WinePredictor.csv")

if __name__ == "__main__":
    main()