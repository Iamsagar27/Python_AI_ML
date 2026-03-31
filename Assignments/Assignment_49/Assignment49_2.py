# 2. Data Preprocessing:
#    - Check and handle missing or zero values in columns like Glucose, Blood Pressure, etc.
#    - Apply feature scaling using StandardScaler or MinMaxScaler.
#    - Split the dataset into features (X) and target (y).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler

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

    TrainDiebetesModel(X,Y)

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

def TrainDiebetesModel(X,Y):
    print("\nFeatures : ", )
    print(X[:5])

    print("\nLabels : ", )
    print(Y[:5])

    print("Shape of X       : ",X.shape)
    print("Shape of Y       : ",Y.shape)

def DiebeticDatasetLoad(DataPath):
    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(DataPath)

    ShowData(df, "Dataset after loading")

def main():
    DiebeticDatasetLoad("diabetes.csv")

if __name__ == "__main__":
    main()