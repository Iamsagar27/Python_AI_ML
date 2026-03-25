# 9. Write a Python program using scikit-learn to generate a classification report for the following data:
# actual = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]
# Display the complete classification report including precision, recall, F1-score, and support.

from sklearn.metrics import classification_report

def main():
    actual_data = [1,1,1,1,0,0,0,0] 
    predicted_data = [1,1,0,1,0,1,0,0]

    print("Classification Report :")
    print(classification_report(actual_data, predicted_data))


if __name__ == "__main__":
    main()