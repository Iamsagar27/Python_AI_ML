# 4. Model Evaluation:
#    - Print accuracy score, confusion matrix, precision, recall, and F1 score.
#    - Use matplotlib or seaborn to visualize confusion matrix.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def DisplayInfo(title):
    print("\n" + "="*70)
    print(title)
    print("="*70)


def ShowData(df, message):
    DisplayInfo(message)

    print("First 5 rows of dataset :")
    print(df.head())

    print("\nShape of dataset :")
    print(df.shape)

    print("\nColumn Names :")
    print(df.columns.tolist())

    print("\nMissing Values in each column :")
    print(df.isnull().sum())

    print("\nBasic Statistics:")
    print(df.describe())

    PlotGraph(df)

    X, Y = DataProcessing(df)

    DiebetesModel(X,Y)

def PlotGraph(df):
    plt.figure()
    sns.countplot(x='Outcome', data=df)
    plt.title("Target Distribution (Outcome)")
    plt.show()

    # Histogram
    df.hist(figsize=(10, 8))
    plt.show()

    # Boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df)
    plt.xticks(rotation=45)
    plt.show()

def DataProcessing(df):
    DisplayInfo("Step 2 : Processing the data")

    cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols] = df[cols].replace(0, np.nan)

    df.fillna(df.median(), inplace=True)

    X = df.drop('Outcome', axis=1)
    y = df['Outcome']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

def DiebetesModel(X,Y):
    print("\nFeatures : ", )
    print(X[:5])

    print("\nLabels : ", )
    print(Y[:5])

    print("Shape of X       : ",X.shape)
    print("Shape of Y       : ",Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test  : ",X_test.shape)
    print("Shape of Y_train : ",Y_train.shape)
    print("Shape of Y_test  : ",Y_test.shape)

    TrainDiebetesModel(X_train, Y_train, X_test, Y_test)

def TrainDiebetesModel(X_train, Y_train, X_test, Y_test):
    DisplayInfo("Step 3 : Training the model")

    models = {}
    
    model_lr = LogisticRegression(max_iter=5000)
    model_dt = DecisionTreeClassifier(random_state=42)
    model_knn = KNeighborsClassifier(n_neighbors=5)

    model_lr.fit(X_train, Y_train)
    model_dt.fit(X_train, Y_train)
    model_knn.fit(X_train, Y_train)

    hard_model = VotingClassifier(
        estimators=[
            ('lr', model_lr),
            ('dt',model_dt),
            ('knn',model_knn)
        ],
        voting="hard"
    )

    hard_model.fit(X_train, Y_train)

    TestDiebetesModel(hard_model, X_test, Y_test)

def TestDiebetesModel(hard_model, X_test, Y_test):
    DisplayInfo("Step 4 : Testing & Evaluation")
    
    y_pred = hard_model.predict(X_test)

    acc = accuracy_score(Y_test, y_pred)
    print("Accuracy:", acc)

    cm = confusion_matrix(Y_test, y_pred)
    print("\nConfusion Matrix:\n", cm)

    print("\nClassification Report:\n", classification_report(Y_test, y_pred))

    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title(" Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    
def DiebeticDatasetLoad(DataPath):
    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(DataPath)

    ShowData(df, "Dataset after loading")

def main():
    DiebeticDatasetLoad("diabetes.csv")

if __name__ == "__main__":
    main()