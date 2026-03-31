# 1. Exploratory Data Analysis (EDA):
#      - Load the dataset using pandas.
#      - Display the first 5 rows.
#      - Show column info and check for null values.
#      - Display basic statistics using.describe().
#      - Plot the distribution of the target variable (Outcome).
#      - Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

def DiebeticDatasetLoad(DataPath):
    df = pd.read_csv(DataPath)

    ShowData(df, "Dataset after loading : ")



def main():
    DiebeticDatasetLoad("diabetes.csv")

if __name__ == "__main__":
    main()