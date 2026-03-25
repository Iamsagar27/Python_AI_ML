# 2. Write a Python program that calculates the variance and standard deviation of the dataset:
# [6, 7, 8, 9, 10, 11, 12]
# Display both results.

import numpy as np

def main():
    dataset = [6, 7, 8, 9, 10, 11, 12]

    variance = np.var(dataset)
    standard_deviation = np.std(dataset)

    print("Variance of the dataset : ", variance)
    print("Standard Deviation of the dataset : ", standard_deviation)

if __name__ == "__main__":
    main()