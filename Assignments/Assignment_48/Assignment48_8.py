# 8. Write a Python program that calculates TP, TN, FP, FN for the following arrays:
# actual = [1,1,1,1,0,0,0,0] predicted = [1,1,0,1,0,1,0,0]
# Display all four values.

from sklearn.metrics import confusion_matrix

def main():
    actual_data = [1,1,1,1,0,0,0,0] 
    predicted_data = [1,1,0,1,0,1,0,0]

    TP = TN = FP = FN = 0

    for i in range(len(actual_data)):
        if actual_data[i] == 1 and predicted_data[i] == 1:
            TP += 1
        elif actual_data[i] == 0 and predicted_data[i] == 0:
            TN += 1
        elif actual_data[i] == 0 and predicted_data[i] == 1:
            FP += 1
        elif actual_data[i] == 1 and predicted_data[i] == 0:
            FN += 1 

    print("True Positive (TP):", TP)
    print("True Negative (TN):", TN)
    print("False Positive (FP):", FP)
    print("False Negative (FN):", FN)

    cm = confusion_matrix(actual_data, predicted_data)
    print("\nConfusion Matrix:\n", cm)


if __name__ == "__main__":
    main()