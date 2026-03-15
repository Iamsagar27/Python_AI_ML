import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

def CheckAccuracy(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    for K in range(1,15):
        model = KNeighborsClassifier(n_neighbors=K)
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)
        Accuracy = accuracy_score(Y_test, Y_pred)
        print("Accuracy for K =",K," is :",Accuracy)

def KNNClassification(DataPath):
    Border = "-"*50

    # Load dataset
    print(Border)
    print("Step 1: Load the dataset")
    print(Border)

    df = pd.read_csv(DataPath)

    print(df.head(10)) 

    # Clean, Prepare and Manipulate data
    print(Border)
    print("Step 2: Clean, Prepare and Manipulate data")
    print(Border)

    print("Dataset after cleaning :")
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    print(df.head(10))
    print(Border)
    print("Total Records : ", df.shape[0])
    print("Total Columns : ", df.shape[1])
    print(Border)

    # Separate Independent and Dependent Variables
    print(Border)
    print("Step 3: Separate Independent and Dependent Variables")
    print(Border)

    le = LabelEncoder()

    df["Whether"] = le.fit_transform(df["Whether"])
    df["Temperature"] = le.fit_transform(df["Temperature"])
    df["Play"] = le.fit_transform(df["Play"])

    print("Data after encoding : \n", df.head())

    X = df[["Whether", "Temperature"]]
    Y = df["Play"]
    
    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)
    print(Border)

    # Train the model
    print(Border)
    print("Step 4 : Train the model")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X, Y)

    # Test the model
    print(Border)
    print("Step 5 : Test the model")
    print(Border)

    test_data = [[2,0]]

    Y_pred = model.predict(test_data)

    if Y_pred[0] == 1:
        print("Prediction : Play")
    else:
        print("Prediction : Don't Play")

    print(Border)

    CheckAccuracy(X,Y)


def main():
    Border = "-"*50

    print(Border)
    print("Play Predictor using KNN")
    print(Border)

    KNNClassification("PlayPredictor.csv")

if __name__ == "__main__":
    main()